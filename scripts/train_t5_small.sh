
#!/usr/bin/env bash
set -euo pipefail

python -m src.training.train --model_name t5-small --epochs 3 --lr 5e-5
