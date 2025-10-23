import fitz  # PyMuPDF
import docx2txt
import os

def extract_text_from_file(file):
    filename = file.filename
    filepath = os.path.join("data", "uploads", filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    file.save(filepath)

    if filename.endswith(".pdf"):
        text = ""
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
    elif filename.endswith(".docx"):
        text = docx2txt.process(filepath)
    else:
        raise ValueError("Unsupported file type. Use PDF or DOCX.")
    return text
