
from ..config import MODEL_NAME
from ..models.transformers import load_model_and_tokenizer

_tok = None
_model = None

def _ensure_loaded():
    global _tok, _model
    if _tok is None or _model is None:
        _tok, _model = load_model_and_tokenizer(MODEL_NAME)

def summarize_text(text: str, max_tokens: int = 128) -> str:
    _ensure_loaded()
    inputs = _tok([text], return_tensors='pt', truncation=True)
    output = _model.generate(**inputs, max_new_tokens=max_tokens)
    return _tok.decode(output[0], skip_special_tokens=True)
