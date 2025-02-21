"""
train_yolo_fine_tune.py
Fine-tune YOLOv8 on your CCPD (or similar) dataset.
Potentially unfreeze layers or tweak advanced hyperparams.
"""

from ultralytics import YOLO

def main():
    # Example: fine-tuning with advanced hyperparameters
    model = YOLO("yolov8n.pt")
    
    # Potential advanced hyperparams, e.g., freeze, custom LR
    model.train(
        data="data/ccpd_yolo.yaml",
        epochs=30,
        batch=16,
        imgsz=640,
        device="cuda",
        project="runs/detect",
        name="ccpd_finetune",
        lr0=0.001,    # custom learning rate
        freeze=0,     # or partial freeze
        patience=5    # early stopping patience
    )

if __name__ == "__main__":
    main()
