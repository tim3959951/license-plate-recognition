"""
train_yolo.py
Train YOLOv8 from scratch on your dataset (e.g., CCPD).
Adjust parameters such as epochs, batch_size, etc.
"""

from ultralytics import YOLO

def main():
    # Example: training from scratch using yolov8n
    model = YOLO("yolov8n.pt")  # or "yolov8s.pt", etc.
    model.train(
        data="data/ccpd_yolo.yaml",  # your YOLO data config
        epochs=50,
        batch=16,
        imgsz=640,
        device="cuda",  # or 'cpu'
        project="runs/detect",
        name="ccpd_train"
    )

if __name__ == "__main__":
    main()
