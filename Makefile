
.PHONY: setup train eval serve test fmt docker

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

train:
	python -m src.training.train --model_name t5-small --epochs 3 --lr 5e-5

eval:
	python -m src.evaluation.evaluate --checkpoint runs/t5-small

serve:
	uvicorn src.deployment.api:app --host 0.0.0.0 --port 8000

test:
	pytest -q

fmt:
	black src tests && isort src tests && flake8 src tests

docker:
	docker build -t mimic-summarizer:latest -f docker/Dockerfile .
