"""
evaluate_yolo.py
Evaluate YOLO detection performance (mAP, precision, recall) on a validation/test set.
"""

from ultralytics import YOLO

def main():
    # Load your trained model
    model = YOLO("runs/detect/ccpd_train/weights/best.pt")  # adjust path
    results = model.val(
        data="data/ccpd_yolo.yaml",  # same config used in training
        split="val"                  # or "test"
    )
    # Print summary metrics
    print("YOLO Evaluation Results:")
    print(f"mAP@0.5: {results.box.map50:.3f}")
    print(f"mAP@0.5:0.95: {results.box.map:.3f}")
    print(f"Precision: {results.box.mp:.3f}")
    print(f"Recall: {results.box.mr:.3f}")

if __name__ == "__main__":
    main()
