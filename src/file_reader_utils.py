import os
import logging
from docx import Document 
import pdfplumber 

logger = logging.getLogger(__name__)


def read_file_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == '.txt':
            with open(file_path, 'r', errors='ignore') as f:
                return f.read()

        elif ext == '.docx':
            doc = Document(file_path)
            return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

        elif ext == '.pdf':
            text = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text)
            return "\n".join(text)

        elif ext == '.doc':
            logger.warning(f".doc format not supported reliably: {file_path}")
            return ""

        else:
            logger.warning(f"Unsupported file extension: {file_path}")
            return ""

    except Exception as e:
        logger.warning(f"Failed to read file {file_path}: {e}")
        return ""
