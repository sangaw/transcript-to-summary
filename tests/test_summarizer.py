from transcript_to_summary.summarizer import summarize_text


def test_summarize_basic():
    text = (
        "Python is a programming language. It is widely used. "
        "Python emphasizes readability. Many developers enjoy using Python."
    )
    summary = summarize_text(text, sentences_count=2)
    assert isinstance(summary, str)
    assert len(summary) > 0


def test_summarize_empty():
    assert summarize_text("", sentences_count=2) == ""
