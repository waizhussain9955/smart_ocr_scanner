from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import ImageResponse, TextDetection
from app.utils import validate_image, preprocess_image, save_processed_image, save_output_json
from app.ocr_service import OCRService
import logging
from typing import Dict, Any
from fastapi import UploadFile, File, HTTPException
import tempfile
import os

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Handwritten OCR API", version="1.0.0")

# CORS - Allow all origins for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OCR service
service = OCRService()

@app.get("/")
async def root():
    return {
        "message": "Smart OCR Scanner API",
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}

@app.post("/extract-text", response_model=ImageResponse)
async def extract_text(file: UploadFile = File(...)) -> Dict[str, Any]:
    try:
        logger.info(f"Received file: {file.filename}, content_type: {file.content_type}")
        
        # Read file content
        contents = await file.read()
        logger.info(f"File size: {len(contents)} bytes")
        
        filename = file.filename or "unknown"
        
        # Validate
        validate_image(contents, filename)
        logger.info(f"File validation passed: {filename}")
        
        # Preprocess
        processed_img = preprocess_image(contents)
        
        # Save to temp directory for Vercel
        temp_dir = tempfile.gettempdir()
        processed_path = os.path.join(temp_dir, f"processed_{filename}")
        import cv2
        cv2.imwrite(processed_path, processed_img)
        logger.info(f"Image preprocessed and saved: {processed_path}")
        
        # OCR
        logger.info("Starting OCR extraction...")
        detections = await service.extract_text(processed_img)
        logger.info(f"OCR completed: found {len(detections)} text detections")
        
        # Response data
        data = {
            "success": True,
            "data": [detection.model_dump() for detection in detections]
        }
        
        # Save JSON to temp
        json_path = os.path.join(temp_dir, f"output_{filename}.json")
        save_output_json(data, json_path)
        
        logger.info(f"Processed {filename}: saved {processed_path}, {json_path}")
        return data
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Processing error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
