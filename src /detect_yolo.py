"""
detect_yolo.py
Use YOLOv8 to detect license plates in new images.
Optionally display or save detection results.
"""

import os
from ultralytics import YOLO

def main():
    model = YOLO("runs/detect/ccpd_train/weights/best.pt")  # your trained model
    source_dir = "data/test/images"  # images to detect
    results = model.predict(
        source=source_dir, 
        save=True, 
        project="runs/detect", 
        name="ccpd_detect"
    )
    # This will create detection images with bounding boxes in runs/detect/ccpd_detect

    print("Detection complete. Check runs/detect/ccpd_detect for results.")

if __name__ == "__main__":
    main()
