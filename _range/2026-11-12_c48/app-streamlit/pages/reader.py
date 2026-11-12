import streamlit as st
from src.translation.document_manager import DocumentManager
from src.reading.reading_session_manager import ReadingSessionManager

def show_reader(book_name):
    st.subheader(f"📖 Lecture : {book_name.replace('_', ' ')}")
    
    if st.button("← Retour à la liste"):
        if "selected_book" in st.session_state:
            del st.session_state.selected_book
        st.switch_page("app/main.py")

    dm = DocumentManager()
    doc = dm.load_document(book_name)
    
    if not doc:
        st.error("Impossible de charger le livre.")
        return

    # Sidebar: Chapter Selector with unique key to prevent rerun issues
    chapter_titles = [f"{ch.number}. {ch.title}" for ch in doc.chapters]
    
    # Use session state to track current chapter to avoid unnecessary reruns
    if f"current_chapter_{book_name}" not in st.session_state:
        st.session_state[f"current_chapter_{book_name}"] = 0
    
    selected_chapter_idx = st.sidebar.selectbox(
        "Chapitres", 
        range(len(chapter_titles)), 
        format_func=lambda x: chapter_titles[x],
        key=f"chapter_selector_{book_name}",
        index=st.session_state[f"current_chapter_{book_name}"]
    )
    
    # Update session state
    st.session_state[f"current_chapter_{book_name}"] = selected_chapter_idx
    
    current_chapter = doc.chapters[selected_chapter_idx]
    
    # Init Session Manager
    rsm = ReadingSessionManager()
    
    # Display Content
    st.markdown("---")
    
    # Display whole chapter content (Scrollable View)
    st.markdown(f"### {current_chapter.title}")
    
    paragraphs = [p for p in current_chapter.paragraphs if p.content.strip()]
    
    if not paragraphs:
        st.warning("Chapitre vide.")
        return

    # --- Audio Player (Fixed at top or just one instance) ---
    if "current_audio_track" in st.session_state:
        st.audio(st.session_state.current_audio_track, autoplay=True)
    
    # --- Chat Interface (Expander or Sidebar) ---
    with st.sidebar.expander("💬 Discuter avec ce chapitre", expanded=False):
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input("Votre question sur ce chapitre ?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            # Simple context preparation
            context = f"Livre: {book_name}\nChapitre: {current_chapter.title}\n\nContexte (début du chapitre): {current_chapter.content[:2000]}..."
            
            from src.llm.llm_client import LLMClient
            llm = LLMClient()
            response = llm.chat([
                {"role": "system", "content": f"Tu es un assistant pédagogique. Réponds aux questions sur le livre en utilisant ce contexte:\n{context}"},
                {"role": "user", "content": prompt}
            ])
            
            # --- Audio Response for Chat ---
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
            
            # Generate audio for the answer
            from src.storage.tts_service import TTSService
            tts = TTSService()
            # Truncate for cost/speed if long
            audio_bytes = tts.generate_audio(response[:1000]) 
            if audio_bytes:
                 st.audio(audio_bytes, autoplay=True)

    # --- Main Content (Scrollable) ---
    # Note: Header is already displayed above, removing duplicate or keeping one.
    
    # --- Translation Logic (Pre-reading) ---
    # We maintain a cache of translated chapters in session_state
    if "translations" not in st.session_state:
        st.session_state.translations = {}
    
    if book_name not in st.session_state.translations:
        st.session_state.translations[book_name] = {}

    display_paragraphs = []
    
    # Check if we need translation
    # If doc has no language set, assume EN.
    doc_lang = getattr(doc, "language", "en")
    
    if doc_lang != "fr":
        if current_chapter.number in st.session_state.translations[book_name]:
            # Load from cache
            display_paragraphs = st.session_state.translations[book_name][current_chapter.number]
            st.success("Chapitre traduit chargé.")
        else:
            # Perfom Translation
            st.info(f"Traduction du chapitre {current_chapter.number} en cours... (Ceci peut prendre un moment)")
            
            from src.llm.llm_client import LLMClient
            llm = LLMClient()
            translated_ps = []
            
            raw_paragraphs = [p for p in current_chapter.paragraphs if p.content.strip()]
            progress_bar = st.progress(0)
            
            for idx, p in enumerate(raw_paragraphs):
                # Translate content
                if p.content.startswith("![]("): 
                    # Image, keep as is
                    trans_text = p.content
                else:
                    trans_text = llm.translate(p.content, target_lang="fr")
                
                # Clone paragraph with new content
                new_p = p.model_copy()
                new_p.content = trans_text
                translated_ps.append(new_p)
                
                # Update progress
                progress_bar.progress((idx + 1) / len(raw_paragraphs))
            
            # Save to cache
            st.session_state.translations[book_name][current_chapter.number] = translated_ps
            display_paragraphs = translated_ps
            progress_bar.empty()
            st.success("✅ Traduction terminée !") 
    else:
        # Already FR
        display_paragraphs = [p for p in current_chapter.paragraphs if p.content.strip()]

    if not display_paragraphs:
        st.warning("Chapitre vide (ou traduction échouée).")
        return

    # --- Content Loop ---
    # --- Global Audio Controls ---
    col_audio_btn, col_status = st.columns([0.2, 0.8])
    with col_audio_btn:
        if st.button("▶ Lire le chapitre", type="primary", use_container_width=True):
             # Collect text from ALL displayed paragraphs (translated ones)
             texts = [p.content for p in display_paragraphs if not p.content.startswith("![](")]
             
             with st.spinner("Génération de l'audio du chapitre..."):
                 full_audio_path = rsm.audio_manager.get_chapter_audio(
                    texts,
                    book_name,
                    current_chapter.number
                 )
             
             if full_audio_path:
                 st.session_state.current_audio_track = full_audio_path
                 st.success("🎧 Audio prêt ! Lecture en cours...")
                 # Force audio display without rerun
                 st.audio(full_audio_path, autoplay=True)

    # --- Content Loop (Text Only) ---
    for i, p in enumerate(display_paragraphs):
        # Clean display without buttons
        content = p.content.strip()
        if content.startswith("![](") and content.endswith(")"):
            image_name = content[4:-1]
            from config.settings import settings
            image_path = settings.OUTPUT_DIR / book_name / image_name
            if image_path.exists():
                st.image(str(image_path), caption=image_name)
            else:
                 st.code(f"Image introuvable : {image_name}") 
        else:
            st.markdown(content, unsafe_allow_html=True)
            
        st.write("")
