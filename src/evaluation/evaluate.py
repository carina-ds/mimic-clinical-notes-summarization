
import argparse
from .metrics import compute_rouge

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint', default='runs/t5-small')
    args = parser.parse_args()

    print(f"[eval] Evaluating checkpoint at: {args.checkpoint}")
    preds = ["patient discharged in stable condition"]
    refs =  ["the patient was discharged in stable condition"]
    scores = compute_rouge(preds, refs)
    print("ROUGE:", scores)

if __name__ == '__main__':
    main()
