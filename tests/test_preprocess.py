
from src.data.preprocess import normalize_text

def test_normalize_text_handles_whitespace():
    text = "HPI:   pt presents  w/  SOB."
    out = normalize_text(text)
    assert "  " not in out
