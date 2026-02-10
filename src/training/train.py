
import argparse
from ..config import MODEL_NAME
from ..utils import seed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', default=MODEL_NAME)
    parser.add_argument('--epochs', type=int, default=3)
    parser.add_argument('--lr', type=float, default=5e-5)
    args = parser.parse_args()

    seed.set_seed(42)
    print(f"[train] Training {args.model_name} for {args.epochs} epochs @ lr={args.lr}")
    # TODO: implement real training loop or HuggingFace Trainer

if __name__ == '__main__':
    main()
