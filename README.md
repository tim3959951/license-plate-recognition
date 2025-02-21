# 🏷️ CCPD License Plate Recognition (YOLO + PaddleOCR)

🚀 **An end-to-end system for license plate detection and recognition using YOLOv8 and PaddleOCR.**  
📌 **Achieved:**  
✅ **mAP@0.5: 99.5% (YOLO Detection Accuracy)**  
✅ **OCR Character Accuracy: 94.75%**  
✅ **Full Plate Recognition Accuracy: 93.26%**  

---

## 📌 Project Overview

| Task                     | Method Used  |
|--------------------------|-------------|
| **License Plate Detection** | YOLOv8 (Fine-tuned) |
| **License Plate Cropping** | Automated via bounding boxes |
| **OCR Recognition** | PaddleOCR (Optimized for Chinese plates) |
| **Accuracy Metrics** | mAP, Precision, Recall, Character Accuracy |
| **Dataset Used** | CCPD (or custom dataset) |

---

## 📂 Project Structure


| File/Folder                  | Description                                                               |
|------------------------------|---------------------------------------------------------------------------|
| `data/`                      | Contains training, validation, test sets, and cropped plate images        |
| ├─ `train/`, `val/`, `test/`| YOLO images & labels (CCPD or custom dataset)                              |
| ├─ `cropped_plates/`         | Cropped plate images after YOLO detection                                 |
| └─ `ground_truth.json`       | Mapping: `{ "cropped_img.jpg": "plate_text" }`                            |
| `visualisation`     | Evaluation  plots & sample detection/OCR images        |
| `src/`                   | Core scripts for YOLO training, detection, OCR, and evaluation            |
| ├─ `train_yolo.py`           | Train YOLO from scratch                                                   |
| ├─ `train_yolo_fine_tune.py` | Fine-tune YOLO on CCPD                                                     |
| ├─ `evaluate_yolo.py`        | Evaluate YOLO detection (mAP, precision, recall)                          |
| ├─ `detect_yolo.py`          | Run YOLO detection on new images                                          |
| ├─ `crop_plates.py`          | Crop detected plate regions                                               |
| ├─ `ocr_paddle.py`           | PaddleOCR text recognition on cropped plates                              |
| └─ `evaluate_ocr.py`         | Compare OCR results vs. ground truth (char-level & full-plate accuracy)   |
| `Lincence Plate Recognition.ipynb`                  | Project documentation (this file)                                         |
| `requirements.txt`           | Python dependencies                                                       |
| `README.md`                  | Project documentation (this file)                                         |

---
## 📊 YOLO Detection Results

🔥 **Example Detection:**  
![YOLO Detection](visualisation/val_batch0_pred.jpg)  

|                                                                                              |                                                                                                 |
|:--------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------:|
| ![Confusion Matrix](visualisation/confusion_matrix.png)<br>🚀 **Confusion Matrix**            | ![PR Curve](visualisation/PR_curve.png)<br>📈 **Precision-Recall Curve**                        |
| ![F1 Score](visualisation/F1_curve.png)<br>📉 **F1 Score Curve**                              | ![P Curve](visualisation/P_curve.png)<br>📌 **P-curve (Precision over training epochs)**        |
| ![R Curve](visualisation/R_curve.png)<br>📌 **R-curve (Recall over training epochs)**         | ![Normalized Confusion Matrix](visualisation/confusion_matrix_normalized.png)<br>📌 **Normalized Confusion Matrix** |

  
---
## YOLO Detection Performance (on test data)

| Metric    | Score   |
|-----------|---------|
| mAP@0.5   | 99.5%   |
| Precision | 99.98%  |
| Recall    | 100%    |

- ✅ **YOLO achieves near-perfect mAP (99.5%)** for license plate detection.  
- ✅ **Extremely high precision (99.98%)** ensures minimal false positives.  
- ✅ **Perfect recall (100%)** indicates the model detects all plates correctly.
---

## 🔠 OCR Performance & Evaluation

### ✅ OCR Recognition Examples

| **Original Image** | **OCR Result** | **Ground Truth** | **Correct?** |
|--------------------|---------------|------------------|--------------|
| ![plate1](visualisation/plate1.jpg) | 皖AYR773 | 皖AYR773 | ✅ |
| ![plate2](visualisation/plate2.jpg) | 皖A406B7 | 皖A406B7 | ✅ |
| ![plate3](visualisation/plate3.jpg) | AZ7711  | 皖AZ7711 | ❌ |


---
## 🆚 OCR Performance Comparison

🔠 **OCR Recognition Performance**
| **OCR Engine**       | **Character Accuracy** | **Full Plate Accuracy** |
|----------------------|----------------------|-------------------------|
| **PaddleOCR**       | **94.75%**            | **93.26%**              |
| **Easy OCR**   | **81.43%**            | **67.98%**              |

📌 **Key Findings:**  
- **PaddleOCR significantly outperforms Easy OCR** in recognizing Chinese license plates.  
- **Easy OCR struggles with small fonts, distortion, and non-English characters.**
- **Post-processing techniques (regex filtering, language models) could further refine PaddleOCR accuracy.**
---

## 🔥 Key Takeaways

📌 **End-to-End Pipeline** – Detection (YOLO) + Recognition (PaddleOCR) in a single workflow.  
📌 **High Accuracy** – **mAP@0.5 = 99.5%**, OCR **Character-Level Accuracy = 94.75%**.  
📌 **Error Analysis & Improvements** – Understanding where OCR struggles.  

---

## 🌍 Real-World Applications

🚗 **Traffic monitoring & toll systems**  
🏢 **Smart parking & automated entry**  
🚓 **Law enforcement & stolen vehicle detection**  

---

## 🛠️ Future Enhancements

🔹 **Improve OCR Accuracy** – Fine-tune PaddleOCR or explore CRNN models.  
🔹 **Post-Processing Rules** – Enforce regex/whitelist filtering for valid plate formats.  
🔹 **Edge Deployment** – Optimize for **Raspberry Pi / Jetson Nano** for real-time use.  

---

## 📖 References

- **[Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)**
- **[PaddleOCR GitHub](https://github.com/PaddlePaddle/PaddleOCR)**
- **[CCPD Dataset](https://github.com/detectRecog/CCPD)**

