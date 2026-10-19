
from pathlib import Path
from io import BytesIO

import pdfplumber
import pytesseract
from PIL import Image


def extract_text(file_path: str) -> str:
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".pdf":
        extracted_pages = []

        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text = page.extract_text() or ""

                if not text.strip():
                    image = page.to_image(resolution=300).original
                    text = pytesseract.image_to_string(image)

                extracted_pages.append(text)

        return "\n".join(extracted_pages).strip()

    elif extension in [".png", ".jpg", ".jpeg"]:
        with Image.open(path) as image:
            return pytesseract.image_to_string(image).strip()

    else:
        raise ValueError(
            "Unsupported file type. Use PDF, PNG, JPG, or JPEG."
        )
