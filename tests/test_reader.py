import os
from transcript_to_summary.reader import read_document


def test_read_txt(tmp_path):
    sample_path = tmp_path / "sample.txt"
    sample_path.write_text("Hello world. This is a test.", encoding="utf-8")
    content = read_document(str(sample_path))
    assert "Hello world" in content


def test_read_unsupported_extension(tmp_path):
    sample_path = tmp_path / "sample.md"
    sample_path.write_text("# Title", encoding="utf-8")
    try:
        read_document(str(sample_path))
        assert False, "Expected ValueError for unsupported extension"
    except ValueError:
        pass
