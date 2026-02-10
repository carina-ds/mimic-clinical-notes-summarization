
import random
import numpy as np

try:
    import torch
except Exception:
    torch = None


def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    if torch is not None:
        try:
            torch.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)
        except Exception:
            pass
