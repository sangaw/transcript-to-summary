from __future__ import annotations

import os
from typing import Optional

from .logger import get_logger

logger = get_logger(__name__)


def _read_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()


def _read_docx(path: str) -> Optional[str]:
    try:
        from docx import Document  # type: ignore
    except Exception:
        logger.warning("python-docx not installed; cannot read DOCX: %s", path)
        return None
    try:
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs)
    except Exception as exc:
        logger.error("Failed to read DOCX %s: %s", path, exc)
        return None


def _read_pdf(path: str) -> Optional[str]:
    try:
        import PyPDF2  # type: ignore
    except Exception:
        logger.warning("PyPDF2 not installed; cannot read PDF: %s", path)
        return None
    try:
        text_parts = []
        with open(path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text_parts.append(page.extract_text() or "")
        return "\n".join(text_parts)
    except Exception as exc:
        logger.error("Failed to read PDF %s: %s", path, exc)
        return None


def read_document(path: str) -> str:
    logger.info("Reading document: %s", path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path not found: {path}")

    extension = os.path.splitext(path)[1].lower()
    if extension == ".txt":
        return _read_txt(path)
    if extension == ".docx":
        content = _read_docx(path)
        if content is not None:
            return content
        raise RuntimeError("DOCX support requires python-docx. Install and retry.")
    if extension == ".pdf":
        content = _read_pdf(path)
        if content is not None:
            return content
        raise RuntimeError("PDF support requires PyPDF2. Install and retry.")

    raise ValueError(f"Unsupported file type: {extension}")
