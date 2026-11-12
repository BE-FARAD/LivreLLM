import streamlit as st
from src.translation.document_manager import DocumentManager
import pages.reader as reader

def show():
    dm = DocumentManager()
    books = dm.list_books()
    
    if not books:
        st.write("La bibliothèque est vide. Allez dans 'Importer'.")
        return
        
    # Grid layout
    cols = st.columns(3)
    for i, book_name in enumerate(books):
        with cols[i % 3]:
            # Loading full doc just for metadata is heavy, simpler version would load just metadata
            # For prototype, load doc
            doc = dm.load_document(book_name)
            if doc:
                with st.container():
                    st.markdown(f"""
                    <div class="book-card">
                        <div style="font-size: 40px;">📘</div>
                        <h3>{book_name.replace("_", " ")}</h3>
                        <p>{len(doc.chapters)} Chapitres</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"Lire", key=book_name, use_container_width=True):
                        st.session_state.selected_book = book_name
                        st.rerun()

    if "selected_book" in st.session_state and st.session_state.selected_book:
        # Redirect to reader (simple switch here as we are in same script logic roughly)
        # But Streamlit separation implies we might need a dedicated page logic or session state switch
        # For simplicity, we create a modal-like full page overwrite or instruct user
        st.divider()
        reader.show_reader(st.session_state.selected_book)
