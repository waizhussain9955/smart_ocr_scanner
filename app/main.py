from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from app.models import ImageResponse, TextDetection
from app.utils import validate_image, preprocess_image, save_processed_image, save_output_json
from app.ocr_service import OCRService
import os
import shutil
from typing import Dict, Any

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Handwritten OCR API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = OCRService()  # Singleton

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}

@app.post("/extract-text", response_model=ImageResponse)
async def extract_text(file: UploadFile = File(...)) -> Dict[str, Any]:
    try:
        logger.info(f"Received file: {file.filename}, content_type: {file.content_type}")
        
        # Validate
        contents = await file.read()
        logger.info(f"File size: {len(contents)} bytes")
        
        filename = file.filename or "unknown"
        validate_image(contents, filename)
        logger.info(f"File validation passed: {filename}")
        
        # Preprocess
        processed_img = preprocess_image(contents)
        processed_path = save_processed_image(processed_img, filename)
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
        
        # Save JSON
        json_path = save_output_json(data, filename)
        
        logger.info(f"Processed {filename}: saved {processed_path}, {json_path}")
        return data
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Processing error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

