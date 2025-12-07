import fitz

def load_pdf(path):
    doc = fitz.open(path)
    return "\n".join(page.get_text("text") for page in doc)
