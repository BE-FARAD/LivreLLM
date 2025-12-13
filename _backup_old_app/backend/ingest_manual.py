import os
import uuid
import shutil
import sys

# Add current directory to sys.path to ensure backend modules can be imported
sys.path.append(os.getcwd())

from backend.routers.books import process_book, UPLOAD_DIR

def ingest_manual():
    source_pdf = "frontend/Data/What-is-Forecasting.pdf"
    
    if not os.path.exists(source_pdf):
        print(f"Error: Source file '{source_pdf}' not found.")
        return

    # Generate ID
    file_id = str(uuid.uuid4())
    print(f"Generated Book ID: {file_id}")

    # Ensure upload dir exists (it should be created by books import, but good to be safe)
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Destination path
    dest_pdf = os.path.join(UPLOAD_DIR, f"{file_id}.pdf")

    # Copy file
    print(f"Copying '{source_pdf}' to '{dest_pdf}'...")
    shutil.copy(source_pdf, dest_pdf)

    # Process
    print("Starting processing...")
    try:
        process_book(file_id, dest_pdf)
        print("Processing complete!")
        print(f"Book ID: {file_id}")
    except Exception as e:
        print(f"Error during processing: {e}")

if __name__ == "__main__":
    ingest_manual()
