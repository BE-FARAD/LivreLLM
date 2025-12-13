import streamlit as st
from src.input.file_watcher import FileWatcher
from src.conversion.marker_converter import MarkerConverter
from src.translation.document_manager import DocumentManager
from src.vectorization.vector_store import VectorStore
import time

def show():
    st.header("Importer un nouveau livre")
    
    fw = FileWatcher()
    new_files = fw.get_new_files()
    
    if not new_files:
        st.info("Aucun fichier PDF trouvé dans `data/01-input`.")
        st.markdown("Déposez vos fichiers PDF dans ce dossier pour commencer.")
        return

    st.write(f"🔍 {len(new_files)} fichier(s) détecté(s)")
    
    for file in new_files:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"📄 **{file['filename']}**")
        with col2:
            if st.button("Importer", key=file['hash']):
                process_book(file)

def process_book(file_info):
    from pathlib import Path
    path = Path(file_info['path'])
    
    status = st.status("Traitement en cours...", expanded=True)
    
    try:
        # 1. Conversion
        status.write("📑 Conversion PDF vers Markdown...")
        converter = MarkerConverter()
        doc = converter.convert(path)
        status.write("✅ Conversion terminée.")
        
        # 2. Sauvegarde
        status.write("💾 Sauvegarde...")
        dm = DocumentManager()
        dm.save_document(doc)
        
        # 3. Vectorisation
        status.write("🧠 Indexation (Vector Store)...")
        vs = VectorStore()
        vs.index_document(doc)
        
        status.update(label="Import terminé !", state="complete", expanded=False)
        st.success(f"Le livre '{doc.book_name}' a été ajouté à la bibliothèque.")
        time.sleep(2)
        st.rerun()
        
    except Exception as e:
        status.update(label="Erreur", state="error")
        st.error(f"Une erreur est survenue : {e}")
        import traceback
        st.code(traceback.format_exc())
