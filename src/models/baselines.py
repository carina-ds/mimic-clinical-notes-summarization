
# Simple extractive baseline

def lead_k(text: str, k: int = 3) -> str:
    sentences = text.split('.')
    return '.'.join(sentences[:k]).strip() + '.'
