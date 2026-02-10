
import re

_WS_RE = re.compile(r"\s+")

def normalize_text(text: str) -> str:
    text = text.replace("​", " ")
    text = _WS_RE.sub(" ", text).strip()
    return text
