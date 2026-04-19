from paddleocr import PaddleOCR
from typing import List
from app.models import TextDetection
import cv2
import numpy as np
from typing import Dict, Any

class OCRService:
    _instance: "OCRService | None" = None
    ocr: Any
    _initialized: bool
    
    def __new__(cls) -> "OCRService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self) -> None:
        if not self._initialized:
            self.ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
            self._initialized = True
    
    async def extract_text(self, processed_img: np.ndarray) -> List[TextDetection]:
        """Extract text from preprocessed image using PaddleOCR."""
        result = self.ocr.ocr(processed_img, cls=True)
        
        detections = []
        if result and result[0]:  # result[0] is list of lines
            for line in result[0]:
                bbox = [[float(p[0]), float(p[1])] for p in line[0]]  # dt_boxes
                rec_text = line[1][0]  # text
                confidence = float(line[1][1])  # confidence
                
                detections.append(
                    TextDetection(
                        text=rec_text,
                        confidence=confidence,
                        bbox=bbox
                    )
                )
        return detections

