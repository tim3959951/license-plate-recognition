"""
crop_plates.py
Use YOLO detection to crop license plate regions from images.
Saves cropped images to data/cropped_plates/.
"""

import os
import cv2
from ultralytics import YOLO

def main():
    model = YOLO("runs/detect/ccpd_train/weights/best.pt")  # or your model path
    source_dir = "data/test/images"
    cropped_dir = "data/cropped_plates"
    os.makedirs(cropped_dir, exist_ok=True)

    image_files = [f for f in os.listdir(source_dir) if f.endswith(".jpg")]
    for img_name in image_files:
        img_path = os.path.join(source_dir, img_name)
        results = model.predict(source=img_path)
        
        # If multiple plates, each box is enumerated
        for r in results:
            for i, box in enumerate(r.boxes.xyxy):
                x_min, y_min, x_max, y_max = map(int, box[:4])
                image = cv2.imread(img_path)
                if image is None:
                    continue
                cropped = image[y_min:y_max, x_min:x_max]
                save_name = f"{img_name.replace('.jpg','')}_plate_{i}.jpg"
                save_path = os.path.join(cropped_dir, save_name)
                cv2.imwrite(save_path, cropped)

    print(f"Cropped plates saved in {cropped_dir}")

if __name__ == "__main__":
    main()
