import streamlit as st
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

st.set_page_config(
    page_title="LivreLLM",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stApp { background-color: #f5f5f7; }
    .book-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        cursor: pointer;
        transition: transform 0.2s;
        text-align: center;
    }
    .book-card:hover { transform: translateY(-5px); }
    h1, h2, h3 { color: #1d1d1f; font-family: -apple-system, sans-serif; }
</style>
""", unsafe_allow_html=True)

st.title("📚 Ma Bibliothèque")

# Sidebar navigation
st.sidebar.title("Menu")
page = st.sidebar.radio("Navigation", ["Bibliothèque", "Importer", "Paramètres"])

if page == "Bibliothèque":
    import pages.library as lib
    lib.show()
elif page == "Importer":
    import pages.import_book as imp
    imp.show()
elif page == "Paramètres":
    st.write("Paramètres (À venir)")
