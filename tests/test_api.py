
from fastapi.testclient import TestClient
from src.deployment.api import app

client = TestClient(app)

def test_summary_endpoint():
    resp = client.post('/summarize', json={"text": "Patient discharged.", "max_tokens": 8})
    assert resp.status_code == 200
    assert 'summary' in resp.json()
