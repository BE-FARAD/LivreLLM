import streamlit as st
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

st.set_page_config(page_title="LivreLLM", page_icon="assets/logo.png", layout="wide", initial_sidebar_state="expanded")

# Initialiser le thème - CLAIR PAR DÉFAUT (Apple Books)
if "theme" not in st.session_state:
    st.session_state.theme = "clair"

# Load CSS de base (style Apple Books - clair)
with open("assets/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Appliquer le MODE SOMBRE si sélectionné
if st.session_state.theme == "sombre":
    st.markdown("""
    <style>
        /* MODE SOMBRE - Alternative au style clair */
        :root {
            --bg-main: #000000;
            --bg-sidebar: #1c1c1e;
            --bg-card: #1c1c1e;
            --text-primary: #ffffff;
            --text-secondary: #98989d;
            --border-color: #38383a;
            --accent-blue: #0a84ff;
            --shadow-light: rgba(0, 0, 0, 0.3);
        }
        
        .stApp {
            background-color: var(--bg-main) !important;
            color: var(--text-primary) !important;
        }
        
        .main .block-container {
            background-color: var(--bg-main) !important;
        }
        
        [data-testid="stSidebar"] {
            background-color: var(--bg-sidebar) !important;
            border-right: 1px solid var(--border-color) !important;
        }
        
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2 {
            color: var(--text-primary) !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-primary) !important;
        }
        
        p, div, span, label, li {
            color: var(--text-primary) !important;
        }
        
        .book-card {
            background: var(--bg-card) !important;
            border: 1px solid var(--border-color) !important;
        }
        
        .book-info {
            background: var(--bg-card) !important;
        }
        
        .book-title {
            color: var(--text-primary) !important;
        }
        
        .book-author, .book-progress {
            color: var(--text-secondary) !important;
        }
        
        .book-content {
            background-color: var(--bg-card) !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
        }
        
        .book-content h1, .book-content h2, .book-content h3 {
            color: var(--text-primary) !important;
        }
        
        .book-content p {
            color: #e8e8e8 !important;
        }
        
        .book-content code {
            background-color: #2c2c2e !important;
            color: #ff9f0a !important;
        }
        
        .stButton > button {
            background-color: var(--accent-blue) !important;
        }
        
        .stButton > button[kind="secondary"] {
            background-color: #2c2c2e !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
        }
        
        .stTextArea textarea {
            background-color: var(--bg-card) !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
        }
        
        .stSelectbox > div > div {
            background-color: var(--bg-card) !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #2c2c2e !important;
            color: var(--text-primary) !important;
        }
        
        ::-webkit-scrollbar-track {
            background: var(--bg-main) !important;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #48484a !important;
        }
    </style>
    """, unsafe_allow_html=True)

# --- HELPERS ---
AUDIO_CACHE_DIR = "audio_cache"
if not os.path.exists(AUDIO_CACHE_DIR): os.makedirs(AUDIO_CACHE_DIR)

def smart_split(text, max_chars=1200):
    # Découpe le texte en segments pour la lecture séquentielle (invisible pour l'utilisateur)
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    for p in paragraphs:
        if len(current_chunk) + len(p) < max_chars:
            current_chunk += p + "\n\n"
        else:
            if current_chunk.strip(): chunks.append(current_chunk.strip())
            current_chunk = p + "\n\n"
    if current_chunk.strip(): chunks.append(current_chunk.strip())
    return chunks

def get_audio_segment(text_segment):
    # Récupère l'audio du segment
    import hashlib
    if not text_segment: return None
    h = hashlib.md5(text_segment.encode()).hexdigest()
    path = os.path.join(AUDIO_CACHE_DIR, f"{h}.mp3")
    if os.path.exists(path): return path
    content = generate_audio_openai(text_segment)
    if content:
        with open(path, "wb") as f: f.write(content)
        return path
    return None

def get_project_root():
    return os.path.dirname(os.path.abspath(__file__))

def get_project_root():
    return os.path.dirname(os.path.abspath(__file__))

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

def get_highlights(book_id, chapter_idx):
    """Récupère les surlignages pour un chapitre"""
    path = os.path.join(LIBRARY_DIR, book_id, f"highlights_chap_{chapter_idx+1}.json")
    if os.path.exists(path):
        with open(path, "r") as f: return json.load(f)
    return []

def save_highlights(book_id, chapter_idx, highlights):
    """Sauvegarde les surlignages pour un chapitre"""
    path = os.path.join(LIBRARY_DIR, book_id, f"highlights_chap_{chapter_idx+1}.json")
    with open(path, "w") as f: json.dump(highlights, f, indent=4)

def apply_highlights(text, highlights):
    """Applique les surlignages sur le texte"""
    if not highlights:
        return text
    
    # Trier par position de fin décroissante pour éviter les conflits d'index
    sorted_highlights = sorted(highlights, key=lambda h: h['end'], reverse=True)
    
    for h in sorted_highlights:
        start, end, color = h['start'], h['end'], h['color']
        if start < len(text) and end <= len(text):
            highlighted = f'<mark style="background-color: {color}; padding: 2px 0;">{text[start:end]}</mark>'
            text = text[:start] + highlighted + text[end:]
    
    return text

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
    
    # Importation du module scanner isolé
    try:
        from core.scanner import scan_pdf_with_marker, cleanup_failed_scan
    except ImportError:
        st.error("Erreur d'importation du module core.scanner. Vérifiez la structure du projet.")
        return

    for pdf_file in pdf_files:
        book_id = pdf_file.replace(".pdf", "").replace(" ", "_").replace("__", "_") # Nettoyage ID
        book_dir = os.path.join(LIBRARY_DIR, book_id)
        
        if not os.path.exists(book_dir):
            os.makedirs(book_dir)
            
            # --- ÉTAPE 1 : SCAN (Conversion PDF -> Markdown) ---
            with st.spinner(f"📑 Scan et conversion de {pdf_file}..."):
                try:
                    input_pdf_path = os.path.join(INPUTS_DIR, pdf_file)
                    
                    # APPEL MODULAIRE : On délègue la complexité à core/scanner.py
                    md_path = scan_pdf_with_marker(input_pdf_path, book_dir)
                    
                    # --- POST-TRAITEMENT CRITIQUE POUR LA VISIBILITÉ ---
                    # 1. Déplacer le MD à la racine si pas déjà le cas
                    final_md_path = os.path.join(book_dir, "content.md")
                    import shutil
                    if md_path != final_md_path:
                        shutil.copy2(md_path, final_md_path)
                        # Copier aussi le dossier d'images s'il existe à côté du md source
                        source_images_dir = os.path.dirname(md_path)
                        if os.path.basename(source_images_dir) != os.path.basename(book_dir):
                             # Si le md était dans un sous-dossier, on ramène tout ce qui est dedans
                             for item in os.listdir(source_images_dir):
                                 s = os.path.join(source_images_dir, item)
                                 d = os.path.join(book_dir, item)
                                 if os.path.exists(d): 
                                     if os.path.isdir(d): shutil.rmtree(d)
                                     else: os.remove(d)
                                 if os.path.isdir(s): shutil.copytree(s, d)
                                 else: shutil.copy2(s, d)

                    # 2. Lire le contenu
                    with open(final_md_path, "r") as f:
                        md_text = f.read()

                    st.success(f"Conversion terminée. Traitement structurel...")

                    # 3. Découpage basique + Metadata (Restauré)
                    # On cherche les lignes commençant par # pour les chapitres
                    import re
                    # Regex simple pour trouver les titres de niveau 1 ou 2
                    chapter_splits = re.split(r'(^# .+)', md_text, flags=re.MULTILINE)
                    
                    chapters = []
                    current_chapter = ""
                    current_title = "Introduction"
                    
                    if len(chapter_splits) > 1:
                        # Le premier élément est souvent l'intro avant le premier titre
                        if chapter_splits[0].strip():
                            chapters.append({"title": "Introduction", "content": chapter_splits[0]})
                        
                        # Ensuite on a des paires (Titre, Contenu)
                        for i in range(1, len(chapter_splits), 2):
                            title = chapter_splits[i].strip().replace("#", "").strip()
                            content = chapter_splits[i+1] if i+1 < len(chapter_splits) else ""
                            chapters.append({"title": title, "content": title + "\n\n" + content})
                    else:
                        chapters = [{"title": "Livre entier", "content": md_text}]
                    
                    # 4. Sauvegarder les chapitres
                    for i, chap in enumerate(chapters):
                        # Sauvegarde FR (pour l'instant on garde l'original comme FR par défaut pour afficher qqch)
                        with open(os.path.join(book_dir, f"chapter_{i+1}_fr.txt"), "w") as f:
                            f.write(chap['content'])
                        # Sauvegarde EN
                        with open(os.path.join(book_dir, f"chapter_{i+1}_en.txt"), "w") as f:
                            f.write(chap['content'])
                            
                    # 5. Créer metadata.json
                    metadata = {
                        "id": book_id,
                        "title": pdf_file.replace(".pdf", "").replace("_", " "),
                        "author": "Inconnu", # Marker ne donne pas l'auteur facilement
                        "summary": chapters[0]['content'][:300] + "...", # Résumé dummy
                        "total_chapters": len(chapters),
                        "processed": True
                    }
                    save_book_metadata(book_id, metadata)
                    
                    # 6. Indexation RAG (Optionnel mais recommandé)
                    try:
                        index_document(md_text, pdf_file)
                    except Exception as e:
                        print(f"RAG Indexing Warning: {e}")

                    # 7. Déplacer le PDF input vers processed
                    processed_dir = os.path.join(INPUTS_DIR, "processed")
                    if not os.path.exists(processed_dir): os.makedirs(processed_dir)
                    shutil.move(input_pdf_path, os.path.join(processed_dir, pdf_file))
                    
                    st.toast(f"Livre {metadata['title']} ajouté à la bibliothèque !", icon="📚")
                    st.rerun()

                except Exception as e:
                    st.error(f"❌ Erreur lors du post-traitement : {e}")
                    import traceback
                    st.code(traceback.format_exc())
                    continue
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
    # Logo
    st.image("assets/logo.png", use_container_width=True)
    st.markdown("<div style='text-align: center; color: #98989d; margin-bottom: 2rem;'>Lellm v1.2</div>", unsafe_allow_html=True)
    
    # Bouton d'action principal
    if st.button("🔄 Scanner les nouveaux livres", type="primary", use_container_width=True):
        process_new_files()
        st.rerun()

    # SECTION OUTILS DE LECTURE (si un livre est ouvert)
    if "selected_book" in st.session_state and st.session_state.selected_book is not None:
        with st.expander("📚 Outils de Lecture", expanded=False): # Fermé par défaut pour être propre
            st.write("**Navigation Rapide**")
            # Ajout des outils de navigation inter-chapitres ici si nécessaire
            
            st.markdown("---")
            st.write("**Surlignage**")
            
            # Initialiser la couleur de surlignage sélectionnée
            if "highlight_color" not in st.session_state:
                st.session_state.highlight_color = "#ffeb3b"
            
            col_h1, col_h2 = st.columns(2)
            with col_h1:
                if st.button("🟡", key="btn_yellow_side", use_container_width=True): st.session_state.highlight_color = "#ffeb3b"
                if st.button("🔵", key="btn_blue_side", use_container_width=True): st.session_state.highlight_color = "#64b5f6"
            with col_h2:
                if st.button("🟢", key="btn_green_side", use_container_width=True): st.session_state.highlight_color = "#81c784"
                if st.button("🟣", key="btn_pink_side", use_container_width=True): st.session_state.highlight_color = "#f48fb1"
                
            if st.button("🗑️ Effacer les notes", use_container_width=True):
                if "current_chapter_idx" in st.session_state:
                    save_highlights(st.session_state.selected_book, st.session_state.current_chapter_idx, [])
                    st.success("Notes effacées")
                    st.rerun()

    # SECTION PARAMÈTRES (En bas)
    st.markdown("<div style='margin-top: auto;'></div>", unsafe_allow_html=True) # Spacer
    with st.expander("⚙️ Paramètres", expanded=False):
        st.write("**Thème**")
        col_theme1, col_theme2 = st.columns(2)
        with col_theme1:
            if st.button("☀️ Clair", key="theme_light_side", use_container_width=True, 
                        type="primary" if st.session_state.theme == "clair" else "secondary"):
                st.session_state.theme = "clair"
                # st.rerun() # Eviter rerun inutile si déjà actif
        with col_theme2:
            if st.button("🌙 Sombre", key="theme_dark_side", use_container_width=True,
                        type="primary" if st.session_state.theme == "sombre" else "secondary"):
                st.session_state.theme = "sombre"
                # st.rerun()
                
        st.markdown("---")
        # Toggle Assistant Vocal
        st.write("**Assistant**")
        if "show_voice_assistant" not in st.session_state: st.session_state.show_voice_assistant = False
        st.session_state.show_voice_assistant = st.toggle("Activer mode vocal", value=st.session_state.show_voice_assistant)


# Le CSS du thème est maintenant chargé au début de l'application

if "selected_book" not in st.session_state: st.session_state.selected_book = None

if st.session_state.selected_book is None:
    # Page d'accueil - Style Apple Books
    st.markdown("<h1 style='margin-bottom: 0.5rem;'>Bibliothèque</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #98989d; font-size: 17px; margin-bottom: 3rem;'>Vos livres et documents</p>", unsafe_allow_html=True)
    
    books = []
    if os.path.exists(LIBRARY_DIR):
        for d in os.listdir(LIBRARY_DIR):
            meta = get_book_metadata(d)
            if meta: books.append(meta)
    
    if not books:
        st.markdown("""
        <div style='text-align: center; padding: 4rem 2rem;'>
            <div style='font-size: 64px; margin-bottom: 1rem;'>📚</div>
            <h2 style='color: #ffffff; margin-bottom: 1rem;'>Aucun livre pour le moment</h2>
            <p style='color: #98989d; font-size: 17px;'>Déposez des PDF dans le dossier <code style='background: #2c2c2e; padding: 4px 8px; border-radius: 6px;'>01_INPUTS</code></p>
            <p style='color: #98989d; font-size: 17px;'>puis cliquez sur "Scanner les nouveaux livres" dans la sidebar</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Grille de livres - 3 colonnes
        cols = st.columns(3, gap="large")
        
        # Couleurs de couverture variées (palette harmonieuse)
        cover_gradients = [
            "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
            "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
            "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
            "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
            "linear-gradient(135deg, #30cfd0 0%, #330867 100%)",
        ]
        
        # Initialiser l'état pour les livres sélectionnés (pour afficher le résumé)
        if "selected_book_preview" not in st.session_state:
            st.session_state.selected_book_preview = None
        
        for i, book in enumerate(books):
            with cols[i % 3]:
                gradient = cover_gradients[i % len(cover_gradients)]
                
                # CRÉATION DE LA CARTE INTERACTIVE (Effet Quizlet/Popover)
                # On utilise un label vide pour le popover mais on injecte le visuel via CSS/hack
                
                # Astuce : On affiche d'abord la carte visuelle
                st.markdown(f"""
                <div class="book-card-container" style="position: relative; margin-bottom: 2rem;">
                    <div class="book-card" style="aspect-ratio: 2/3; background: {gradient}; border-radius: 12px; padding: 20px; display: flex; flex-direction: column; justify-content: flex-end; box-shadow: 0 4px 15px rgba(0,0,0,0.1); transition: transform 0.2s;">
                        <div style="font-size: 40px; margin-bottom: auto;">📖</div>
                        <div style="color: white; font-weight: bold; font-size: 18px; line-height: 1.3; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">{book['title']}</div>
                        <div style="color: rgba(255,255,255,0.9); font-size: 14px; margin-top: 5px;">{book.get('author', 'Auteur inconnu')}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Le bouton popover est placé juste en dessous (ou dessus si on pouvait) pour l'interaction
                with st.popover("👆 Cliquer pour lire", use_container_width=True):
                    # CONTENU DU "DOS" DE LA CARTE
                    st.markdown(f"### {book['title']}")
                    st.caption(f"✍️ {book.get('author', 'Auteur inconnu')} • {book['total_chapters']} chapitres")
                    st.markdown("---")
                    st.markdown(f"**Résumé :**")
                    st.markdown(f"{book['summary']}")
                    st.markdown("---")
                    if st.button(f"🚀 COMMENCER LA LECTURE", key=f"read_{book['id']}", type="primary", use_container_width=True):
                        st.session_state.selected_book = book['id']
                        st.rerun()
else:
    book_id = st.session_state.selected_book
    meta = get_book_metadata(book_id)
    
    # EN-TÊTE OPTIMISÉE - Bouton retour et sélecteur sur la première ligne
    col_back, col_chapter, col_tabs = st.columns([1.5, 2, 2])
    
    with col_back:
        if st.button("← Retour à la bibliothèque", use_container_width=True):
            st.session_state.selected_book = None
            st.rerun()
    
    with col_chapter:
        current_chapter_label = st.selectbox(
            "Chapitre",
            [f"Chapitre {i+1}" for i in range(meta['total_chapters'])],
            label_visibility="collapsed"
        )
        chapter_idx = int(current_chapter_label.split(" ")[1]) - 1
    
    with col_tabs:
        tab_choice = st.radio(
            "Langue",
            ["🇫🇷 Français", "🇬🇧 Original"],
            horizontal=True,
            label_visibility="collapsed"
        )
    
    
    # Titre du livre - AU DESSUS du contenu
    st.markdown(f"<h1 style='margin: 0.75rem 0 0.5rem 0; font-size: 24px; font-weight: 600; color: var(--text-primary);'>{meta['title']}</h1>", unsafe_allow_html=True)
    
    
    
    # Sauvegarder l'index du chapitre pour la sidebar
    st.session_state.current_chapter_idx = chapter_idx
    
    # Chemins des fichiers
    chapter_path = os.path.join(LIBRARY_DIR, book_id, f"chapter_{chapter_idx+1}.txt")
    fr_chapter_path = os.path.join(LIBRARY_DIR, book_id, f"chapter_{chapter_idx+1}_fr.txt")
    audio_path = os.path.join(LIBRARY_DIR, book_id, f"audio_chap_{chapter_idx+1}.mp3")
    
    if os.path.exists(chapter_path):
        with open(chapter_path, "r") as f: content = f.read()
        
        # Affichage du contenu selon la langue choisie
        if tab_choice == "🇬🇧 Original":
            # Afficher le texte ORIGINAL (anglais)
            # Utilisation d'un seul bloc pour éviter les erreurs de DOM "removeChild"
            st.markdown(f'<div class="book-content">\n\n{content}\n\n</div>', unsafe_allow_html=True)
                
        else:  # Français
            fr_content = ""
            if os.path.exists(fr_chapter_path):
                with open(fr_chapter_path, "r") as f: fr_content = f.read()
                
                # AFFICHAGE CONTENU (Texte Complet - Le visuel ne change pas)
                st.markdown(f'<div class="book-content">\n\n{fr_content}\n\n</div>', unsafe_allow_html=True)
                
                # --- AUDIO INTELLIGENT (Backend invisible) ---
                st.markdown("---")
                
                # Setup Chunking Backend
                chunks = smart_split(fr_content, max_chars=2000)
                if "reading_pos" not in st.session_state: st.session_state.reading_pos = 0
                if "book_autoplay" not in st.session_state: st.session_state.book_autoplay = False
                
                # Contrôles Simple
                c1, c2 = st.columns([1, 4])
                with c1:
                    # Bouton simple : Lecture / Pause
                    btn_label = "⏸️ PAUSE" if st.session_state.book_autoplay else "▶️ Écouter le chapitre"
                    if st.button(btn_label, key=f"smart_play_{chapter_idx}", type="primary" if not st.session_state.book_autoplay else "secondary"):
                        st.session_state.book_autoplay = not st.session_state.book_autoplay
                        # Reset stop flag on manual play
                        if st.session_state.book_autoplay: st.session_state.force_stop_audio = False
                        st.rerun()
                
                with c2:
                    if st.session_state.book_autoplay:
                        st.caption(f"Lecture en cours... (Partie {st.session_state.reading_pos + 1}/{len(chunks)})")

                # --- MOTEUR DE LECTURE ---
                if st.session_state.book_autoplay:
                    # 1. Check for Interruptions (Hook: User spoke)
                    if st.session_state.get("force_stop_audio", False):
                        st.session_state.book_autoplay = False
                        st.session_state.force_stop_audio = False
                        st.rerun()
                    
                    # 2. Play Current Chunk
                    current_idx = st.session_state.reading_pos
                    if 0 <= current_idx < len(chunks):
                        segment_path = get_audio_segment(chunks[current_idx])
                        if segment_path:
                            st.audio(segment_path, autoplay=True)
                            
                            # Hidden Next Button for JS to click
                            if st.button("NextChunkHidden", key="next_chunk_automaton", help="Hidden"):
                                st.session_state.reading_pos += 1
                                st.rerun()

                            # JS Auto-Next Logic
                            js = """
                            <script>
                                const audios = window.parent.document.querySelectorAll('audio');
                                if (audios.length > 0) {
                                    const audio = audios[audios.length - 1];
                                    audio.onended = function() { 
                                        const btns = window.parent.document.querySelectorAll('button');
                                        btns.forEach(b => { if(b.innerText === "NextChunkHidden") b.click(); });
                                    };
                                }
                                // Hide the Ugly Button
                                const btns = window.parent.document.querySelectorAll('button');
                                btns.forEach(b => { if(b.innerText === "NextChunkHidden") b.style.display = 'none'; });
                            </script>
                            """
                            st.components.v1.html(js, height=0)
                            
            else:
                st.warning("⚠️ Ce chapitre n'est pas encore traduit.")
                
                # Bouton de traduction
                if st.button("🌐 Traduire ce chapitre (IA)", key=f"trans_{chapter_idx}", type="primary"):
                    with st.spinner("Traduction du chapitre en cours..."):
                        if os.path.exists(chapter_path):
                            with open(chapter_path, "r") as f: en_text = f.read()
                            try:
                                prompt_text = en_text[:20000]
                                system_msg = "Tu es un expert technique. Traduis ce contenu en français en gardant le formatage."
                                completion = client_openai.chat.completions.create(
                                    model="gpt-4o",
                                    messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": prompt_text}]
                                )
                                with open(fr_chapter_path, "w") as f: f.write(completion.choices[0].message.content)
                                st.success("Traduction terminée !")
                                st.rerun()
                            except Exception as e: st.error(f"Erreur : {e}")
                        else: st.error("Source introuvable.")


    # --- CHAT WITH LLM ---
    st.markdown("---")
    st.subheader("💬 Discussion avec le LLM")
    
    if "messages" not in st.session_state: st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]): st.markdown(message["content"])
    
    # Chat écrit (toujours visible)
    user_input = st.chat_input("💬 Posez votre question sur le livre...")
    
    # Assistant Vocal (masqué par défaut, affichable via Paramètres)
    if "show_voice_assistant" in st.session_state and st.session_state.show_voice_assistant:
        st.markdown("### 🎤 Mode Vocal")
        
        col_v1, col_v2 = st.columns([4, 1])
        with col_v1:
            audio_input = st.audio_input("Parlez pour poser une question", key="voice_input")
        with col_v2:
            # Bouton d'interruption
            if st.button("⏹️ STOP", type="secondary", use_container_width=True, help="Arrêter la lecture en cours"):
                st.session_state.force_stop_audio = True
                st.rerun()

        if audio_input is not None:
            # Traitement de l'audio
            audio_bytes = audio_input.read()
            audio_size = len(audio_bytes)
            
            # Créer un hash pour détecter les duplicatas
            import hashlib
            audio_hash = hashlib.md5(audio_bytes).hexdigest()
            
            if "last_audio_hash" not in st.session_state:
                st.session_state.last_audio_hash = None
            
            if st.session_state.last_audio_hash != audio_hash:
                st.session_state.last_audio_hash = audio_hash
                st.session_state.force_stop_audio = False 
                
                # --- HOOK: INTERRUPTION QUESTION ---
                # Si le livre est en cours de lecture, on PAUSE et on marque pour reprise
                if st.session_state.get("book_autoplay", False):
                    st.session_state.resume_after_qa = True
                    st.session_state.book_autoplay = False # STOP BOOK
                else:
                    st.session_state.resume_after_qa = False
                # -----------------------------------

                if audio_size < 5000:
                    st.warning("⚠️ L'audio semble vide. Vérifiez vos permissions micro.")
                else:
                    with st.spinner("Transcription en cours..."):
                        transcription = transcribe_audio_openai(audio_bytes)
                        if transcription:
                            user_input = transcription
                        else:
                            st.error("❌ Échec de la transcription")
    
    # Traitement de l'input (audio ou texte)
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"): st.markdown(user_input)
        
        response = get_llm_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"): st.markdown(response)
        
        if "show_voice_assistant" in st.session_state and st.session_state.show_voice_assistant:
            # Vérifier si on doit jouer l'audio du LLM
            if not st.session_state.get("force_stop_audio", False):
                audio_response = generate_audio_openai(response)
                if audio_response: 
                    st.audio(audio_response, autoplay=True)
                    
                    # --- HOOK: REPRISE LECTURE ---
                    if st.session_state.get("resume_after_qa", False):
                         st.toast("📖 Reprise de la lecture...", icon="▶️")
                         import time
                         time.sleep(3.5) # Délai pour laisser finir la phrase du LLM
                         st.session_state.book_autoplay = True
                         st.session_state.resume_after_qa = False
                         st.rerun()
                    # -----------------------------

            else:
                st.session_state.force_stop_audio = False # Reset for next turn
                
        st.rerun()
