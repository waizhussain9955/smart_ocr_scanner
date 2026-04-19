@echo off
echo ========================================
echo  Smart OCR Scanner - Quick Start
echo ========================================
echo.

echo [1/3] Starting Backend Server...
echo Backend will be available at: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.

start cmd /k "cd /d %~dp0 && venv\Scripts\activate && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

timeout /t 5 /nobreak >nul

echo [2/3] Starting Flutter App...
echo.

cd smart_ocr_scanner
start cmd /k "flutter run -d windows"

echo.
echo [3/3] Done!
echo.
echo Both Backend and Frontend are starting...
echo.
echo To stop the servers, close the terminal windows.
echo.
pause
