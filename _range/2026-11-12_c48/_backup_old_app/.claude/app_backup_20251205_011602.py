import streamlit as st
from streamlit_mic_recorder import mic_recorder
import openai
import os
from dotenv import load_dotenv
import io
from pypdf import PdfReader
import json
import time
import uuid
from qdrant_client import QdrantClient
from qdrant_client.http import models
from fastembed import TextEmbedding

# Load environment variables
load_dotenv()

# Configure OpenAI API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Directories
INPUTS_DIR = "01_INPUTS"
LIBRARY_DIR = "library_data"
if not os.path.exists(INPUTS_DIR): os.makedirs(INPUTS_DIR, exist_ok=True)
if not os.path.exists(LIBRARY_DIR): os.makedirs(LIBRARY_DIR, exist_ok=True)

st.set_page_config(page_title="LivreLLM", page_icon="📚", layout="wide", initial_sidebar_state="expanded")

# Load CSS
with open("assets/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- VECTOR DB SETUP ---
@st.cache_resource
def get_vector_db():
    client = QdrantClient(path="local_qdrant_db")
    embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    return client, embedding_model

try:
    client, embedding_model = get_vector_db()
    COLLECTION_NAME = "books_collection"
    VECTOR_SIZE = 384
    
    try:
        collections = client.get_collections().collections
        exists = any(c.name == COLLECTION_NAME for c in collections)
        if not exists:
            client.create_collection(collection_name=COLLECTION_NAME, vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE))
    except:
        try: client.create_collection(collection_name=COLLECTION_NAME, vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE))
        except: pass
except Exception as e:
    st.error(f"Erreur DB: {e}")

# --- BACKEND FUNCTIONS ---

def get_book_metadata(book_id):
    path = os.path.join(LIBRARY_DIR, book_id, "metadata.json")
    if os.path.exists(path):
        with open(path, "r") as f: return json.load(f)
    return None

def save_book_metadata(book_id, metadata):
    path = os.path.join(LIBRARY_DIR, book_id, "metadata.json")
    with open(path, "w") as f: json.dump(metadata, f, indent=4)

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += (chunk_size - overlap)
    return chunks

def index_document(text, filename):
    chunks = chunk_text(text)
    points = []
    embeddings = list(embedding_model.embed(chunks))
    
    for i, (chunk, vector) in enumerate(zip(chunks, embeddings)):
        points.append(models.PointStruct(
            id=str(uuid.uuid4()),
            vector=vector.tolist(),
            payload={"text": chunk, "filename": filename}
        ))
    
    client.upsert(collection_name=COLLECTION_NAME, points=points)

def retrieve_context(query, limit=3):
    try:
        query_vector = list(embedding_model.embed([query]))[0]
        hits = client.search(collection_name=COLLECTION_NAME, query_vector=query_vector.tolist(), limit=limit)
        return [f"[Extrait de {hit.payload.get('filename', 'Livre')}]\n{hit.payload['text']}" for hit in hits]
    except: return []

def process_new_files():
    pdf_files = [f for f in os.listdir(INPUTS_DIR) if f.endswith(".pdf")]
    
    import shutil
    # Import marker (lazy load to avoid startup delay if not used)
    try:
        from marker.convert import convert_single_pdf
        from marker.models import load_all_models
    except ImportError:
        st.error("Marker-pdf n'est pas installé. Lancez `pip install marker-pdf`.")
        return

    # Cache models to avoid reloading
    @st.cache_resource
    def get_marker_models():
        return load_all_models()

    for pdf_file in pdf_files:
        book_id = pdf_file.replace(".pdf", "").replace(" ", "_")
        book_dir = os.path.join(LIBRARY_DIR, book_id)
        images_dir = os.path.join(book_dir, "images")
        
        if not os.path.exists(book_dir):
            os.makedirs(book_dir)
            if not os.path.exists(images_dir): os.makedirs(images_dir)
            
            # 1. Convert PDF to Markdown with Marker
            with st.spinner(f"Conversion haute fidélité de {pdf_file} avec Marker (cela peut prendre du temps)..."):
                try:
                    model_lst = get_marker_models()
                    full_text, images, out_meta = convert_single_pdf(
                        os.path.join(INPUTS_DIR, pdf_file),
                        model_lst,
                        max_pages=None,
                        batch_multiplier=2
                    )
                    
                    # Save images
                    for filename, image in images.items():
                        save_path = os.path.join(images_dir, filename)
                        image.save(save_path)
                        
                    md_text = full_text
                except Exception as e:
                    st.error(f"Erreur Marker: {e}. Fallback sur pymupdf4llm.")
                    import pymupdf4llm
                    md_text = pymupdf4llm.to_markdown(
                        os.path.join(INPUTS_DIR, pdf_file),
                        write_images=True,
                        image_path=images_dir,
                        image_format="png"
                    )

            # 2. Split into Chapters (using Markdown headers)
            # We look for # Chapter or # Partie or just big headers
            chapters = []
            current_chapter = []
            lines = md_text.split('\n')
            
            # Simple heuristic: Split on H1 or H2 headers that look like chapters
            import re
            header_pattern = r"^(#|##)\s+(Chapter|Chapitre|Partie|Part|\d+\.).*$"
            
            for line in lines:
                if re.match(header_pattern, line, re.IGNORECASE):
                    if current_chapter:
                        chapters.append("\n".join(current_chapter))
                    current_chapter = [line]
                else:
                    current_chapter.append(line)
            
            if current_chapter: chapters.append("\n".join(current_chapter))
            
            # Fallback if no chapters found
            if len(chapters) <= 1:
                # Split by length (approx 10k chars ~ 5 pages)
                chapters = []
                chunk_size = 10000
                for i in range(0, len(md_text), chunk_size):
                    chapters.append(md_text[i:i+chunk_size])
            
            # Save Chapters & Translate Immediately
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, chapter_content in enumerate(chapters):
                # Save Original
                with open(os.path.join(book_dir, f"chapter_{i+1}.txt"), "w") as f:
                    f.write(chapter_content)
                
                # Translate to French
                status_text.text(f"Traduction du chapitre {i+1}/{len(chapters)}...")
                try:
                    clean_prompt = f"""
                    Tu es un expert technique et traducteur.
                    TA TÂCHE : Traduire et Formater ce contenu technique en FRANÇAIS.
                    
                    CONSIGNES STRICTES DE FORMATAGE :
                    1. **MATHÉMATIQUES** : Repère les formules et réécris-les proprement en LaTeX (entre $$ pour les blocs, $ pour le texte).
                    2. **CODE** : Repère les blocs de code et entoure-les de triples backticks (```python, etc.). NE TRADUIS PAS LE CODE, traduis seulement les commentaires.
                    3. **STRUCTURE** : Garde les titres Markdown (#, ##).
                    4. **TEXTE** : Traduis les explications en français fluide.
                    
                    TEXTE BRUT À TRAITER :
                    {chapter_content[:15000]} 
                    """
                    # Limit to 15k chars to avoid token limits for now
                    
                    fr_content = client_openai.chat.completions.create(
                        model="gpt-4o", messages=[{"role": "system", "content": clean_prompt}]
                    ).choices[0].message.content
                    
                    with open(os.path.join(book_dir, f"chapter_{i+1}_fr.txt"), "w") as f:
                        f.write(fr_content)
                except Exception as e:
                    print(f"Erreur traduction chap {i+1}: {e}")
                
                progress_bar.progress((i + 1) / len(chapters))
            
            status_text.text("Indexation RAG...")
            
            # Index for RAG (using the full markdown text)
            index_document(md_text, pdf_file)
            
            # Generate Summary
            summary_prompt = f"Fais un résumé court et accrocheur (2 phrases) en FRANÇAIS de ce livre : {chapters[0][:2000]}..."
            try:
                summary = client_openai.chat.completions.create(
                    model="gpt-4o", messages=[{"role": "system", "content": summary_prompt}]
                ).choices[0].message.content
            except: summary = "Résumé non disponible."
            
            metadata = {
                "id": book_id,
                "title": pdf_file.replace(".pdf", "").replace("_", " "),
                "author": "Inconnu",
                "summary": summary,
                "total_chapters": len(chapters),
                "processed_at": time.time()
            }
            save_book_metadata(book_id, metadata)

# Configure OpenAI Client
from openai import OpenAI
try:
    client_openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    st.error(f"Erreur init OpenAI: {e}")
    client_openai = None

# ... (rest of code)

def transcribe_audio_openai(audio_bytes):
    if not client_openai: return None
    try:
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = "audio.wav" 
        transcript = client_openai.audio.transcriptions.create(model="whisper-1", file=audio_file, language="fr")
        return transcript.text
    except Exception as e:
        st.error(f"Erreur Transcription: {e}")
        return None

def get_llm_response(text):
    if not client_openai: return "Erreur: Client OpenAI non initialisé."
    try:
        context_chunks = retrieve_context(text)
        context_str = "\n\n".join(context_chunks)
        system_prompt = "Tu es un assistant vocal expert. Utilise le CONTEXTE fourni pour répondre."
        if context_str: system_prompt += f"\n\nCONTEXTE:\n{context_str}"
        completion = client_openai.chat.completions.create(model="gpt-4o", messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": text}])
        return completion.choices[0].message.content
    except Exception as e: return f"Désolé, erreur: {str(e)}"

def generate_audio_openai(text):
    if not client_openai: return None
    try:
        response = client_openai.audio.speech.create(model="tts-1", voice="alloy", input=text)
        return response.content
    except: return None

# --- UI LOGIC ---

with st.sidebar:
    st.title("Bibliothèque")
    st.write("📂 Dossier: `01_INPUTS/`")
    if st.button("🔄 Scanner les nouveaux livres"):
        with st.spinner("Traitement en cours..."):
            process_new_files()
            st.success("Scan terminé !")
            time.sleep(1)
            st.rerun()
    
    st.markdown("---")
    st.subheader("Mes Livres")
    if os.path.exists(LIBRARY_DIR):
        books_list = [get_book_metadata(d) for d in os.listdir(LIBRARY_DIR) if get_book_metadata(d)]
        for book in books_list:
            if st.button(f"📘 {book['title']}", key=f"nav_{book['id']}"):
                st.session_state.selected_book = book['id']
                st.rerun()

if "selected_book" not in st.session_state: st.session_state.selected_book = None

if st.session_state.selected_book is None:
    st.title("Accueil")
    st.write("Vos livres récents")
    books = []
    if os.path.exists(LIBRARY_DIR):
        for d in os.listdir(LIBRARY_DIR):
            meta = get_book_metadata(d)
            if meta: books.append(meta)
    
    if not books: st.info("Aucun livre trouvé. Déposez des PDF dans le dossier '01_INPUTS' et cliquez sur Scanner.")
    else:
        cols = st.columns(3)
        for i, book in enumerate(books):
            with cols[i % 3]:
                st.markdown(f"""<div class="book-card"><div class="book-title">{book['title']}</div><div class="book-author">{book['summary'][:100]}...</div></div>""", unsafe_allow_html=True)
                if st.button(f"Ouvrir", key=f"btn_{book['id']}"):
                    st.session_state.selected_book = book['id']
                    st.rerun()

else:
    book_id = st.session_state.selected_book
    meta = get_book_metadata(book_id)
    
    if st.button("← Retour à la bibliothèque"):
        st.session_state.selected_book = None
        st.rerun()
        
    st.title(meta['title'])
    
    col_nav, col_content = st.columns([1, 3])
    
    with col_nav:
        st.subheader("Chapitres")
        current_chapter = st.radio("Aller à", [f"Chapitre {i+1}" for i in range(meta['total_chapters'])], label_visibility="collapsed")
        chapter_idx = int(current_chapter.split(" ")[1]) - 1
    
    with col_content:
        chapter_path = os.path.join(LIBRARY_DIR, book_id, f"chapter_{chapter_idx+1}.txt")
        fr_chapter_path = os.path.join(LIBRARY_DIR, book_id, f"chapter_{chapter_idx+1}_fr.txt")
        audio_path = os.path.join(LIBRARY_DIR, book_id, f"audio_chap_{chapter_idx+1}.mp3")
        
        if os.path.exists(chapter_path):
            with open(chapter_path, "r") as f: content = f.read()
            
            tab_fr, tab_en = st.tabs(["🇫🇷 Version Française", "🇬🇧 Original"])
            with tab_en: st.text_area("Texte Original", content, height=600)
            with tab_fr:
                fr_content = ""
                if os.path.exists(fr_chapter_path):
                    with open(fr_chapter_path, "r") as f: fr_content = f.read()
                    st.text_area("Texte Français", fr_content, height=600)
                else:
                    st.info("Ce chapitre n'a pas encore été traduit.")
                    if st.button("📄 Traduire et Formater (Maths/Code)"):
                        with st.spinner("Analyse, Traduction et Formatage en cours..."):
                            clean_prompt = f"""
                            Tu es un expert technique et traducteur.
                            TA TÂCHE : Traduire et Formater ce contenu technique en FRANÇAIS.
                            
                            CONSIGNES STRICTES DE FORMATAGE :
                            1. **MATHÉMATIQUES** : Repère les formules (souvent mal extraites du PDF) et réécris-les proprement en LaTeX (entre $$ pour les blocs, $ pour le texte).
                            2. **CODE** : Repère les blocs de code et entoure-les de triples backticks (```python, ```java, etc.). NE TRADUIS PAS LE CODE (noms de variables, fonctions), traduis seulement les commentaires.
                            3. **STRUCTURE** : Utilise des titres Markdown (#, ##) pour respecter la hiérarchie du document.
                            4. **TEXTE** : Traduis les explications en français fluide et pédagogique.
                            
                            TEXTE BRUT À TRAITER :
                            {content[:4000]}... (tronqué pour performance)
                            """
                            fr_content = client_openai.chat.completions.create(
                                model="gpt-4o", messages=[{"role": "system", "content": clean_prompt}]
                            ).choices[0].message.content
                            
                            with open(fr_chapter_path, "w") as f:
                                f.write(fr_content)
                            st.rerun()
                
                # Audio Player & Generation
                if st.button(f"▶️ Traduire et Écouter {current_chapter}"):
                    with st.spinner("Traduction et Génération audio..."):
                        # 1. Translate if needed
                        if not fr_content:
                            clean_prompt = f"""
                            Tu es un expert technique. Traduis ce texte en FRANÇAIS.
                            - Formate les maths en LaTeX ($$).
                            - Formate le code en blocs Markdown (```).
                            - Ne traduis pas le code lui-même.
                            TEXTE: {content[:4000]}...
                            """
                            fr_content = client_openai.chat.completions.create(
                                model="gpt-4o", messages=[{"role": "system", "content": clean_prompt}]
                            ).choices[0].message.content
                            
                            with open(fr_chapter_path, "w") as f:
                                f.write(fr_content)
                        
                        # 2. Generate Audio (Ask TTS to ignore heavy code/math markup reading)
                        if not os.path.exists(audio_path):
                            # Create a "Reading Script" that skips complex code reading
                            reading_prompt = f"Transforme ce texte technique en un script de lecture audio fluide. Résume les blocs de code par 'Le code montre...' et lis les formules mathématiques de façon naturelle. Texte : {fr_content[:4000]}"
                            reading_script = client_openai.chat.completions.create(
                                model="gpt-4o", messages=[{"role": "system", "content": reading_prompt}]
                            ).choices[0].message.content
                            
                            response = client_openai.audio.speech.create(model="tts-1", voice="alloy", input=reading_script)
                            response.stream_to_file(audio_path)
                        
                        st.audio(audio_path, autoplay=True)
                        if not os.path.exists(fr_chapter_path): st.rerun()
                
                if os.path.exists(audio_path): st.audio(audio_path)

    # --- VOICE ASSISTANT (CHAT) ---
    st.markdown("---")
    st.subheader("💬 Assistant Vocal")
    
    if "messages" not in st.session_state: st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]): st.markdown(message["content"])
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write("Parlez :")
        audio = mic_recorder(start_prompt="🎙️ Enregistrer", stop_prompt="⏹️ Stop", key='recorder')
    
    user_input = st.chat_input("Posez une question sur le livre...")
    
    final_input = None
    if audio:
        if "last_audio_id" not in st.session_state or st.session_state.last_audio_id != audio['id']:
            st.session_state.last_audio_id = audio['id']
            final_input = transcribe_audio_openai(audio['bytes'])
    if user_input: final_input = user_input
    
    if final_input:
        st.session_state.messages.append({"role": "user", "content": final_input})
        with st.chat_message("user"): st.markdown(final_input)
        
        with st.spinner("Réflexion..."):
            ai_response = get_llm_response(final_input)
        
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant"): st.markdown(ai_response)
        
        audio_bytes = generate_audio_openai(ai_response)
        if audio_bytes: st.audio(audio_bytes, format="audio/mp3", autoplay=True)
