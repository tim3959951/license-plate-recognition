"""
detect_yolo.py
Run YOLOv8 to detect license plates on new images, optionally save results.
"""

import os
from ultralytics import YOLO

def main():
    model = YOLO("runs/detect/ccpd_train/weights/best.pt")
    source_dir = "data/test/images"
    results = model.predict(
        source=source_dir,
        save=True,
        project="runs/detect",
        name="ccpd_detect"
    )
    print("Detection complete. Check runs/detect/ccpd_detect for results.")

if __name__ == "__main__":
    main()
