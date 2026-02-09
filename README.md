
# Summarizing Physician Notes with MIMIC

**Goal:** Train and deploy a clinical summarization model that produces concise, clinically useful summaries of physician notes (e.g., discharge summaries), while following responsible AI practices.

## Highlights
- Transformer-based abstractive summarization (T5/Pegasus/BART)
- Robust preprocessing for noisy clinical text
- Objective (ROUGE/BERTScore) + optional human evaluation
- FastAPI inference service + Docker image
- Model Card and ethics documentation

## Data Access (MIMIC)
This repository **does not** contain any MIMIC data. To reproduce:
1. Complete the required training and apply for access on PhysioNet (MIMIC-IV Notes).
2. Place files under `data/raw/` (see `data/README.md`).

> Respect all usage restrictions and never push protected data to GitHub.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Quickstart
```bash
bash scripts/prepare_data.sh
bash scripts/train_t5_small.sh
bash scripts/evaluate.sh
uvicorn src.deployment.api:app --host 0.0.0.0 --port 8000
```
