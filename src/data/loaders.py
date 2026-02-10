
from pathlib import Path
from typing import Iterable, Dict
import json

from . import preprocess


def iter_notes(jsonl_path: Path) -> Iterable[Dict]:
    """Yield notes from a JSONL file with keys like {"subject_id", "hadm_id", "text"}."""
    with jsonl_path.open() as f:
        for line in f:
            yield json.loads(line)
