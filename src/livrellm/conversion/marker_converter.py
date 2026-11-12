import re
from pathlib import Path
from typing import List
from livrellm.conversion.markdown_document import MarkdownDocument
from livrellm.conversion.chapter import Chapter, Paragraph
from config.settings import settings

# Since marker is a CLI tool usually, we invoke it or import it if possible.
# Ideally we import it. If 'marker-pdf' is installed, we can try to use its python API 
# or subprocess if API is unstable. For this implementation, let's assume subprocess 
# for stability as marker API changes often.
import subprocess

class MarkerConverter:
    """Handles conversion of PDF to Markdown using Marker."""
    
    def __init__(self, output_dir: Path = settings.OUTPUT_DIR):
        self.output_dir = output_dir
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)

    def convert(self, pdf_path: Path) -> MarkdownDocument:
        """Converts a PDF file to a MarkdownDocument object."""
        book_name = pdf_path.stem.replace(" ", "_")
        book_output_dir = self.output_dir / book_name
        
        # Ensure output dir exists
        book_output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"Converting {pdf_path} to {book_output_dir}...")
        
        # NOTE: Using marker via CLI subprocess because it's robust.
        # marker_single /path/to/file.pdf /path/to/output --batch_multiplier 2 --max_pages 20 # example
        # check installed marker command. Usually 'marker_single'.
        
        cmd = [
            "marker_single",
            str(pdf_path.absolute())
        ]
        
        # We run in the output directory so marker creates its folder there, 
        # or outputs files there.
        # Note: marker usually creates a folder matching the filename.
        # So we set cwd to self.output_dir (02-output)
        
        try:
            # Removed capture_output=True to see progress in logs
            subprocess.run(cmd, check=True, cwd=self.output_dir)
        except subprocess.CalledProcessError as e:
            # Les deux lignes qui suivaient le premier `raise` etaient
            # inatteignables : le message detaille n'a jamais ete affiche
            # (C48, phase 0). On garde le detail, et on leve **une** fois.
            detail = e.stderr.decode(errors="replace") if e.stderr else "(pas de sortie d'erreur)"
            print(f"Marker Error: {detail}")
            raise

        # Read the output markdown.
        # Sometimes marker outputs as 'pdf_name.md' or inside a subfolder.
        # Marker usually creates output_dir/pdf_name/pdf_name.md
        possible_md = book_output_dir / pdf_path.stem / f"{pdf_path.stem}.md"
        
        if not possible_md.exists():
            # Fallback search
            mdown_files = list(book_output_dir.rglob("*.md"))
            if not mdown_files:
                raise FileNotFoundError("Marker failed to produce a .md file")
            possible_md = mdown_files[0]
            
        content = possible_md.read_text(encoding="utf-8")
        
        # Parse structure
        chapters = self._parse_chapters(content)
        
        doc = MarkdownDocument(
            book_name=book_name,
            language="en", # Default, detection later
            content=content,
            chapters=chapters,
            file_path=str(possible_md)
        )
        return doc

    def _parse_chapters(self, text: str) -> List[Chapter]:
        """
        Parses chapters based on headers, avoiding code comments.
        """
        lines = text.split('\n')
        chapters = []
        current_num = 1
        current_title = "Introduction"
        current_content = []
        
        in_code_block = False
        
        for line in lines:
            stripped = line.strip()
            
            # Toggle code block state
            if stripped.startswith("```"):
                in_code_block = not in_code_block
            
            # Check for headers ONLY if not in code block
            is_header = False
            if not in_code_block:
                if line.startswith("# ") or line.startswith("## "):
                    # Extra heuristic: ignore if it looks like a variable assignment or code comment that slipped through
                    # But broadly, # Space is a header in MD.
                    is_header = True
            
            if is_header:
                if current_content:
                    # Save previous chapter
                    full_text = "\n".join(current_content)
                    chapters.append(Chapter(
                        number=current_num,
                        title=current_title,
                        content=full_text,
                        paragraphs=self._parse_paragraphs(full_text, current_num)
                    ))
                    current_num += 1
                
                # Clean title (remove # and potential span tags)
                clean_title = line.replace("#", "").strip()
                # Remove HTML spans if present in title
                clean_title = re.sub(r'<span[^>]*>.*?</span>', '', clean_title).strip()
                
                current_title = clean_title
                current_content = [line]
            else:
                current_content.append(line)
                
        # Last chapter
        if current_content:
            full_text = "\n".join(current_content)
            chapters.append(Chapter(
                number=current_num,
                title=current_title,
                content=full_text,
                paragraphs=self._parse_paragraphs(full_text, current_num)
            ))
            
        return chapters

    def _parse_paragraphs(self, chapter_text: str, chapter_num: int) -> List[Paragraph]:
        """Splits chapter text into logical paragraphs."""
        raw_paras = chapter_text.split('\n\n')
        paras = []
        p_num = 1
        for p in raw_paras:
            if p.strip():
                paras.append(Paragraph(
                    number=p_num,
                    content=p.strip()
                ))
                p_num += 1
        return paras
