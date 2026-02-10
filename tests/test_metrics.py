
from src.evaluation.metrics import compute_rouge

def test_compute_rouge_basic():
    pred = ["patient discharged in stable condition"]
    ref  = ["the patient was discharged in stable condition"]
    scores = compute_rouge(pred, ref)
    assert "rougeL" in scores
