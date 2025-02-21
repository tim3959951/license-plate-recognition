"""
evaluate_ocr.py
Compare OCR results vs. ground_truth.json to compute character-level and full-plate accuracy.
"""

import os
import json
import cv2
from paddleocr import PaddleOCR

def main():
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    cropped_dir = "data/cropped_plates"
    gt_path = "data/ground_truth.json"

    with open(gt_path, "r", encoding="utf-8") as f:
        ground_truths = json.load(f)

    total_chars = 0
    correct_chars = 0
    total_plates = len(ground_truths)
    correct_plates = 0

    for image_name, true_text in ground_truths.items():
        img_path = os.path.join(cropped_dir, image_name)
        plate_image = cv2.imread(img_path)
        if plate_image is None:
            print(f"❌ Failed to load {image_name}")
            continue

        results = ocr.ocr(plate_image)
        if not results:
            detected_text = ""
        else:
            detected_text = "".join(
                [line[1][0] for res in results for line in res if line]
            ).strip()

        # Clean strings (remove spaces, dots, etc.)
        true_clean = true_text.replace("·","").replace(" ","").replace(".","").replace("-","")
        detect_clean = detected_text.replace("·","").replace(" ","").replace(".","").replace("-","")

        # Character-level accuracy
        total_chars += len(true_clean)
        min_len = min(len(true_clean), len(detect_clean))
        correct_chars += sum(1 for i in range(min_len) if true_clean[i] == detect_clean[i])

        # Full-plate accuracy
        if true_clean == detect_clean:
            correct_plates += 1

        print(f"GT (raw): {true_text} | OCR (raw): {detected_text}")
        print(f"GT (clean): {true_clean} | OCR (clean): {detect_clean}\n")

    char_accuracy = correct_chars / total_chars if total_chars else 0
    plate_accuracy = correct_plates / total_plates if total_plates else 0

    print("\nOCR Evaluation Results:")
    print(f"Character Accuracy: {char_accuracy:.2%}")
    print(f"Full Plate Accuracy: {plate_accuracy:.2%}")

if __name__ == "__main__":
    main()
