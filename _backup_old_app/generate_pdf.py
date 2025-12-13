import fitz  # PyMuPDF

doc = fitz.open()
page = doc.new_page()
text = "Bonjour. Ceci est un livre de test pour l'application LivreLLM. L'intelligence artificielle devrait lire ce texte."
page.insert_text((50, 50), text, fontsize=12)
doc.save("test_book.pdf")
print("Created test_book.pdf")
