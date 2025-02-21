# 🏷️ CCPD License Plate Recognition (YOLO + PaddleOCR)

This project demonstrates **Chinese license plate detection and recognition** using the [CCPD dataset](https://github.com/detectRecog/CCPD) (or a similar dataset). It combines **YOLOv8** for plate detection and **PaddleOCR** for text recognition. The pipeline focuses on **end-to-end efficiency**, from training and detection to OCR evaluation.

---

## 🚀 Project Overview

- **Objective**: Detect and recognize license plates in a real-world dataset (CCPD or similar).
- **Techniques**:  
  - **YOLOv8** for bounding box detection  
  - **PaddleOCR** for text recognition  
  - **Cropping** and **evaluation** scripts for a clean workflow
- **Key Features**:  
  - Fine-tuning YOLO for improved detection accuracy  
  - Automatic plate cropping for OCR  
  - JSON-based ground truth mapping for easy evaluation  
- **Potential Use Cases**:  
  - **Traffic monitoring**, **Parking systems**, **Smart city** applications

---

## 📂 Project Structure

| File/Folder                  | Description                                                               |
|------------------------------|---------------------------------------------------------------------------|
| `data/`                      | Contains training, validation, test sets, and cropped plate images        |
| ├─ `train/`, `val/`, `test/`| YOLO images & labels (CCPD or custom dataset)                              |
| ├─ `cropped_plates/`         | Cropped plate images after YOLO detection                                 |
| └─ `ground_truth.json`       | Mapping: `{ "cropped_img.jpg": "plate_text" }`                            |
| `scripts/`                   | Core scripts for YOLO training, detection, OCR, and evaluation            |
| ├─ `train_yolo.py`           | Train YOLO from scratch                                                   |
| ├─ `train_yolo_fine_tune.py` | Fine-tune YOLO on CCPD                                                     |
| ├─ `evaluate_yolo.py`        | Evaluate YOLO detection (mAP, precision, recall)                          |
| ├─ `detect_yolo.py`          | Run YOLO detection on new images                                          |
| ├─ `crop_plates.py`          | Crop detected plate regions                                               |
| ├─ `ocr_paddle.py`           | PaddleOCR text recognition on cropped plates                              |
| └─ `evaluate_ocr.py`         | Compare OCR results vs. ground truth (char-level & full-plate accuracy)   |
| `requirements.txt`           | Python dependencies                                                       |
| `README.md`                  | Project documentation (this file)                                         |
| `docs/images/` (optional)    | Place sample detection/OCR images for demonstration in the README         |

---

## 🔬 Implementation Steps

1. **(Optional) Train YOLO**  
   - Run `scripts/train_yolo.py` or `scripts/train_yolo_fine_tune.py`.  
   - Produces weights in `runs/detect/.../weights/best.pt`.

2. **(Optional) Evaluate YOLO**  
   - `python scripts/evaluate_yolo.py`  
   - Checks detection metrics (mAP, precision, recall) on `data/val` or `data/test`.

3. **Detect Plates**  
   - `python scripts/detect_yolo.py`  
   - Uses the trained model to find bounding boxes on new images.

4. **Crop Plates**  
   - `python scripts/crop_plates.py`  
   - Reads YOLO bounding boxes, crops plate regions, and saves to `data/cropped_plates/`.

5. **OCR with PaddleOCR**  
   - `python scripts/ocr_paddle.py`  
   - Performs text recognition on each cropped plate image.

6. **Evaluate OCR**  
   - `python scripts/evaluate_ocr.py`  
   - Compares recognized text to `ground_truth.json`, computing character-level and full-plate accuracy.

---

## 📈 YOLO & OCR Performance

- **YOLO**: Achieves ~90% mAP on CCPD (depending on hyperparameters).  
- **OCR**:  
  - **Character Accuracy** ~94.75%  
  - **Full Plate Accuracy** ~93.26%  

### Example Visualization
If you have sample images, you can showcase them:

```md
![YOLO detection sample](docs/images/yolo_detection.png)
```
## 🔥 Key Takeaways

1. **End-to-End Pipeline**  
   - From detection (YOLO) to recognition (PaddleOCR) in a single workflow.  

2. **Cropped Plate Approach**  
   - Isolates the region of interest for more accurate OCR performance.  

3. **JSON Ground Truth**  
   - Simplifies the evaluation of OCR accuracy with a `{filename: plate_text}` mapping.  

4. **Potential Real-World Applications**  
   - **Traffic flow analysis**, **parking management**, **smart city** solutions, and more.

---

## 🌍 Why It Matters

- **Automation**  
  - Automates license plate reading, saving labor in law enforcement or toll collection.  

- **Scalability**  
  - YOLO + OCR can handle large city networks or real-time edge deployments.  

- **Efficiency**  
  - Reduces manual review; improved accuracy fosters reliable data analytics in transportation systems.

---

## 🛠️ Future Directions

- **Advanced Data Augmentation**  
  - Improve YOLO detection under adverse conditions (nighttime, motion blur, etc.).

- **Fine-Tune PaddleOCR**  
  - Train on specialized license plate fonts or add a custom dictionary to reduce OCR errors.

- **Regex/Whitelist Post-Processing**  
  - Enforce valid plate formats (e.g., provinces, letter-digit patterns) to refine OCR results.

- **Edge Deployment**  
  - Test on low-power devices (Raspberry Pi, Jetson Nano) for on-site, real-time recognition.

---

## 📖 References

- **[Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)**
- **[PaddleOCR GitHub](https://github.com/PaddlePaddle/PaddleOCR)**
- **[CCPD Dataset](https://github.com/detectRecog/CCPD)**
