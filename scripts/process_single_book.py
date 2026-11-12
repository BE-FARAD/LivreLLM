import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from livrellm.conversion.marker_converter import MarkerConverter
from livrellm.translation.document_manager import DocumentManager
from livrellm.vectorization.vector_store import VectorStore
from config.settings import settings

def process_single_book(filename):
    input_path = settings.INPUT_DIR / filename
    if not input_path.exists():
        print(f"Error: File {filename} not found in {settings.INPUT_DIR}")
        return

    print(f"🚀 Starting processing for: {filename}")

    try:
        # 1. Conversion
        print("📑 1. Converting PDF to Markdown (this may take a while)...")
        converter = MarkerConverter()
        doc = converter.convert(input_path)
        print("✅ Conversion done.")

        # 2. Save
        print("💾 2. Saving Document...")
        dm = DocumentManager()
        dm.save_document(doc)
        print("✅ Document saved.")

        # 3. Vectorization
        print("🧠 3. Indexing in Vector Store...")
        vs = VectorStore()
        vs.index_document(doc)
        print("✅ Indexing done.")

        print(f"\n🎉 SUCCESS: Book '{doc.book_name}' is ready in the Library!")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    file_to_process = "Learning LangChain Building AI and LLM Applications with LangChain and LangGraph (Mayo Oshin, Nuno Campos) (Z-Library).pdf"
    process_single_book(file_to_process)
