from __future__ import annotations

import argparse
import os
from typing import Optional

from .logger import get_logger
from .reader import read_document
from .summarizer import summarize_text, summarize_document

logger = get_logger(__name__)


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read a document and provide a summary.")
    parser.add_argument("--input", required=True, help="Path to input file (.txt, .docx, .pdf)")
    parser.add_argument("--sentences", type=int, default=3, help="Number of sentences in summary")
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    try:
        extension = os.path.splitext(args.input)[1].lower()
        if extension == ".docx":
            result = summarize_document(args.input, sentences_count=max(1, args.sentences))
        else:
            text = read_document(args.input)
            result = summarize_text(text, sentences_count=max(1, args.sentences))
        print(result)
        return 0
    except Exception as exc:
        logger.exception("Failed to summarize: %s", exc)
        return 1
