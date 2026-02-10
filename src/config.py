
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data'
RAW_DIR = DATA_DIR / 'raw'
INTERIM_DIR = DATA_DIR / 'interim'
PROCESSED_DIR = DATA_DIR / 'processed'
RESULTS_DIR = ROOT / 'results'
MODELS_DIR = ROOT / 'models'

MODEL_NAME = os.getenv('MODEL_NAME', 't5-small')
SEED = 42
