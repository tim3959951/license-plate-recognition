"""
decode_ccpd.py
Decode CCPD filenames to get the correct license plate text, then generate ground_truth.json.
This is crucial if you rely on CCPD's embedded indices (e.g., 0_0_25_3_25_24_27).
"""

import os
import json

# Example CCPD dictionaries:
provinces = [
    "皖","沪","津","渝","冀","晋","蒙","辽","吉","黑",
    "苏","浙","京","闽","赣","鲁","豫","鄂","湘","粤",
    "桂","琼","川","贵","云","藏","陕","甘","青","宁","新"
]

alphadigit = [
    '0','1','2','3','4','5','6','7','8','9',
    'A','B','C','D','E','F','G','H','J','K',
    'L','M','N','P','Q','R','S','T','U','V',
    'W','X','Y','Z'
]

def decode_plate_from_filename(filename):
    """
    Remove any '_plate_xxx' suffix, then parse the index sequence (e.g. 0_0_25_3_25_24_27).
    Returns a string like '皖A12345'.
    """
    base = os.path.splitext(filename)[0]
    if "_plate_" in base:
        base = base.split("_plate_")[0]
    
    parts = base.split('-')
    # Typically, CCPD's index is at parts[4], but confirm for your dataset
    plate_indices_str = parts[4]  # e.g. "0_0_25_3_25_24_27"
    idxs = list(map(int, plate_indices_str.split('_')))

    # idxs[0] => province, idxs[1] => second char, idxs[2:] => rest
    plate_str = provinces[idxs[0]] + alphadigit[idxs[1]]
    for r in idxs[2:]:
        plate_str += alphadigit[r]
    return plate_str

def main():
    label_dir = "data/test/labels"       # or your label folder
    cropped_dir = "data/cropped_plates"
    ground_truth = {}

    # For each label .txt, find matching cropped images that share a prefix
    for label_file in os.listdir(label_dir):
        if not label_file.endswith(".txt"):
            continue
        prefix = label_file.replace(".txt", "")
        
        # e.g. "xxxxx-0_0_25_3_25_24_27-xx_plate_0.jpg"
        matched_imgs = [
            f for f in os.listdir(cropped_dir)
            if f.startswith(prefix) and f.endswith(".jpg")
        ]
        if not matched_imgs:
            print(f"No cropped images found for prefix '{prefix}'")
            continue
        
        for img_name in matched_imgs:
            plate_text = decode_plate_from_filename(img_name)
            ground_truth[img_name] = plate_text
            print(f"Decoded {img_name} -> {plate_text}")
    
    # Write out ground_truth.json
    json_path = "data/ground_truth.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(ground_truth, f, indent=4, ensure_ascii=False)
    
    print(f"Generated {json_path}")

if __name__ == "__main__":
    main()
