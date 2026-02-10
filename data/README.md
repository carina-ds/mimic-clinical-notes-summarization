
# Data Directory

- `raw/`       : place de-identified source notes here (local only; .gitignored)
- `interim/`   : intermediate artifacts after cleaning/normalization
- `processed/` : tokenized/train-ready datasets (local only; .gitignored)

## Getting MIMIC
1. Complete the required training and credentialing on PhysioNet for **MIMIC-IV** and the **Note** module.
2. Request and obtain access.
3. Use `scripts/prepare_data.sh` to structure text into JSONL/CSV for training.

**Do not** commit any files from `raw/`, `interim/`, or `processed/`.
