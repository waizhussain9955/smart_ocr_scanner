import cv2  # type: ignore
import numpy as np  # type: ignore
import os
import json
from datetime import datetime
from PIL import Image  # type: ignore
import io

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def validate_image(file_bytes: bytes, filename: str) -> bool:
    """Validate image file size and type."""
    if len(file_bytes) > MAX_FILE_SIZE:
        raise ValueError("File size exceeds 5MB limit")
    allowed_types = {'.jpg', '.jpeg', '.png'}
    ext = os.path.splitext(filename.lower())[1]
    if ext not in allowed_types:
        raise ValueError("Only JPG and PNG files allowed")
    try:
        Image.open(io.BytesIO(file_bytes))
        return True
    except:
        raise ValueError("Invalid image file")

def preprocess_image(img_bytes: bytes) -> np.ndarray:
    """Preprocess image: grayscale, Gaussian blur, Otsu threshold."""
    img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def save_processed_image(processed_img: np.ndarray, filename: str) -> str:
    """Save processed image to /processed folder."""
    os.makedirs("processed", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_filename = f"processed/{timestamp}_{filename}"
    cv2.imwrite(out_filename, processed_img)
    return out_filename

def save_output_json(data: dict, filename: str) -> str:
    """Save output JSON to /outputs folder or specified path."""
    # Check if filename is a full path
    if filename.endswith('.json'):
        # It's already a full path (for Vercel temp directory)
        out_filename = filename
    else:
        # It's just a filename, save to outputs folder
        os.makedirs("outputs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_filename = f"outputs/{timestamp}_{filename}.json"
    
    with open(out_filename, 'w') as f:
        json.dump(data, f, indent=2)
    return out_filename

