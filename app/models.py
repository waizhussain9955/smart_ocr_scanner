from pydantic import BaseModel  # type: ignore
from typing import List

class TextDetection(BaseModel):
    text: str
    confidence: float
    bbox: List[List[float]]

class ImageResponse(BaseModel):
    success: bool
    data: List[TextDetection]

