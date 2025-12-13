import json
import re
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from config.settings import settings

def clean_text(text):
    # Remove <span ...></span> tags
    # Pattern: <span id="page-X-Y"></span> or similar
    # We want to remove the tag entirely, and any surrounding extra spaces if needed.
    cleaned = re.sub(r'<span[^>]*>.*?</span>', '', text)
    # Also clean up double hashes if they were separated by the span, e.g. "##  Title" -> "## Title"
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def clean_structure(data):
    # Clean chapters
    for chapter in data.get('chapters', []):
        chapter['title'] = clean_text(chapter['title'])
        # Clean chapter full content
        if 'content' in chapter:
            chapter['content'] = clean_text(chapter['content'])
            
        # Clean paragraphs
        for p in chapter.get('paragraphs', []):
            p['content'] = clean_text(p['content'])
            
    # Clean top level content if present
    if 'content' in data:
        data['content'] = clean_text(data['content'])
    return data

def fix_json():
    # Target specific file
    json_path = settings.OUTPUT_DIR / "Learning_LangChain_Building" / "json" / "Learning_LangChain_Building.json"
    
    if not json_path.exists():
        print(f"❌ JSON file not found: {json_path}")
        return

    print(f"🔧 Fixing {json_path}...")
    
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    cleaned_data = clean_structure(data)
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=2, ensure_ascii=False)
        
    print("✅ JSON content cleaned.")

if __name__ == "__main__":
    fix_json()
