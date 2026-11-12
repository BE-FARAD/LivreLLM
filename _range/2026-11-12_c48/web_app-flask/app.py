from flask import Flask, render_template, jsonify, request, send_file
from pathlib import Path
import sys

# Add project root
sys.path.append(str(Path(__file__).parent.parent))

from src.translation.document_manager import DocumentManager
from src.reading.reading_session_manager import ReadingSessionManager
from src.llm.llm_client import LLMClient
from config.settings import settings

app = Flask(__name__, 
    template_folder='templates',
    static_folder='static'
)

# Global state (in production, use Redis/sessions)
current_sessions = {}

@app.route('/')
def index():
    """Library page"""
    dm = DocumentManager()
    books = dm.list_books()
    return render_template('library.html', books=books)

@app.route('/reader/<book_name>')
def reader(book_name):
    """Reader page"""
    dm = DocumentManager()
    doc = dm.load_document(book_name)
    
    if not doc:
        return "Livre introuvable", 404
    
    return render_template('reader.html', 
        book_name=book_name,
        book_title=book_name.replace('_', ' '),
        language=doc.language
    )

@app.route('/api/book/<book_name>/chapters')
def get_chapters(book_name):
    """Get all chapters for a book"""
    dm = DocumentManager()
    doc = dm.load_document(book_name)
    
    if not doc:
        return jsonify({'error': 'Book not found'}), 404
    
    chapters = [
        {
            'number': ch.number,
            'title': ch.title,
            'content': ch.content
        }
        for ch in doc.chapters
    ]
    
    return jsonify({
        'book_name': book_name,
        'language': doc.language,
        'chapters': chapters
    })

@app.route('/api/book/<book_name>/chapter/<int:chapter_num>')
def get_chapter(book_name, chapter_num):
    """Get a specific chapter"""
    dm = DocumentManager()
    doc = dm.load_document(book_name)
    
    if not doc:
        return jsonify({'error': 'Book not found'}), 404
    
    chapter = next((ch for ch in doc.chapters if ch.number == chapter_num), None)
    
    if not chapter:
        return jsonify({'error': 'Chapter not found'}), 404
    
    # Extract paragraphs
    paragraphs = [
        {
            'number': p.number,
            'content': p.content
        }
        for p in chapter.paragraphs if p.content.strip()
    ]
    
    return jsonify({
        'number': chapter.number,
        'title': chapter.title,
        'paragraphs': paragraphs
    })

@app.route('/api/audio/<book_name>/chapter/<int:chapter_num>', methods=['POST'])
def generate_chapter_audio(book_name, chapter_num):
    """Generate audio for entire chapter"""
    data = request.json
    texts = data.get('texts', [])
    
    rsm = ReadingSessionManager()
    audio_path = rsm.audio_manager.get_chapter_audio(
        texts,
        book_name,
        chapter_num
    )
    
    if audio_path:
        return jsonify({'audio_url': f'/audio/{book_name}/chapter/{chapter_num}/file'})
    
    return jsonify({'error': 'Audio generation failed'}), 500

@app.route('/audio/<book_name>/chapter/<int:chapter_num>/file')
def serve_audio(book_name, chapter_num):
    """Serve audio file"""
    # Find the audio file
    audio_dir = settings.AUDIO_DIR / book_name
    
    # Find the FULL chapter file (with hash)
    audio_files = list(audio_dir.glob(f"{book_name}_ch{chapter_num:02d}_FULL_*.mp3"))
    
    if audio_files:
        return send_file(audio_files[0], mimetype='audio/mpeg')
    
    return "Audio not found", 404

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat questions with improved context"""
    data = request.json
    question = data.get('question')
    book_name = data.get('book_name')
    chapter_num = data.get('chapter_num')
    history = data.get('history', [])  # Chat history
    
    # Load chapter context
    dm = DocumentManager()
    doc = dm.load_document(book_name)
    current_chapter = next((ch for ch in doc.chapters if ch.number == chapter_num), None)
    
    if not current_chapter:
        return jsonify({'error': 'Chapter not found'}), 404
    
    # Build rich context
    context_parts = [
        f"Livre: {book_name.replace('_', ' ')}",
        f"Chapitre {current_chapter.number}: {current_chapter.title}",
        "",
        "Contenu du chapitre:",
        current_chapter.content[:3000] + ("..." if len(current_chapter.content) > 3000 else "")
    ]
    
    # Add context from adjacent chapters if relevant
    if chapter_num > 1:
        prev_chapter = next((ch for ch in doc.chapters if ch.number == chapter_num - 1), None)
        if prev_chapter:
            context_parts.append(f"\nChapitre précédent: {prev_chapter.title}")
    
    context = "\n".join(context_parts)
    
    # Build messages with history
    messages = [
        {
            "role": "system", 
            "content": (
                "Tu es un assistant pédagogique expert. Réponds aux questions sur le livre "
                "de manière claire et pédagogique. Base-toi sur le contexte fourni. "
                "Si la réponse n'est pas dans le contexte, explique ce que tu sais et suggère "
                "où chercher plus d'informations.\n\n"
                f"Contexte:\n{context}"
            )
        }
    ]
    
    # Add conversation history (last 5 exchanges max)
    for msg in history[-10:]:
        messages.append(msg)
    
    # Add current question
    messages.append({"role": "user", "content": question})
    
    llm = LLMClient()
    response = llm.chat(messages)
    
    return jsonify({
        'answer': response,
        'chapter': {
            'number': current_chapter.number,
            'title': current_chapter.title
        }
    })

@app.route('/images/<book_name>/<image_name>')
def serve_image(book_name, image_name):
    """Serve book images"""
    image_path = settings.OUTPUT_DIR / book_name / image_name
    
    if image_path.exists():
        return send_file(image_path)
    
    return "Image not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
