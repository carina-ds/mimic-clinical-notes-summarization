
# Summarizing Physician Notes with MIMIC

**Goal:** Train and deploy a clinical summarization model that produces concise, clinically-useful summaries of physician notes (e.g., discharge summaries), while following responsible AI practices.

## 🚀 Highlights
- Transformer-based abstractive summarization (T5/Pegasus)
- Robust preprocessing for noisy clinical text
- Objective (ROUGE/BERTScore) and human evaluation
- FastAPI inference service + Docker image
- Model Card and ethics documentation (healthcare compliance mindset)

## 🏥 Data Access (MIMIC)
This repository **does not** contain any MIMIC data. To reproduce:
1. Complete the required training and apply for access on PhysioNet.
2. Place files under `data/raw/` (see `data/README.md`).

> ⚠️ Respect all usage restrictions and never push protected data to GitHub.

## 📦 Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pre-commit install
``
