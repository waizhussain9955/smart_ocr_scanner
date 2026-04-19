# 📱 Smart OCR Scanner - AI-Powered Text Extraction

A modern, production-ready mobile application that uses AI-powered OCR (Optical Character Recognition) to extract text from images. Built with Flutter for the frontend and FastAPI with PaddleOCR for the backend.

## ✨ Features

- 📸 **Camera Capture**: Take photos directly from the app
- 🖼️ **Gallery Upload**: Select existing images from your device
- 🤖 **AI-Powered OCR**: Uses PaddleOCR for accurate text extraction
- 📊 **Confidence Scores**: See accuracy percentage for each detected text
- 📋 **Copy to Clipboard**: Easily copy extracted text
- 💾 **History**: Automatically saves your scan history
- 🎨 **Modern UI**: Beautiful Material Design 3 interface
- 📱 **Cross-Platform**: Works on Android, iOS, Windows, macOS, Linux, and Web

## 📸 Screenshots

*(Add your screenshots here)*

## 🏗️ Project Structure

```
moblie-app/
├── app/                      # Backend (FastAPI + PaddleOCR)
│   ├── main.py              # FastAPI application entry point
│   ├── models.py            # Pydantic data models
│   ├── utils.py             # Image processing utilities
│   └── ocr_service.py       # PaddleOCR service
├── smart_ocr_scanner/       # Frontend (Flutter)
│   ├── lib/
│   │   ├── config/          # App configuration
│   │   ├── screens/         # UI screens
│   │   └── services/        # API and business logic
│   └── pubspec.yaml         # Flutter dependencies
├── vercel.json              # Vercel deployment configuration
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- **Backend**: Python 3.10 or higher
- **Frontend**: Flutter 3.10 or higher
- **For Android Development**: Android SDK
- **For iOS Development**: Xcode (macOS only)

### Backend Setup

1. **Clone the repository**:
```bash
git clone https://github.com/YOUR_USERNAME/smart-ocr-scanner.git
cd smart-ocr-scanner
```

2. **Create virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the backend server**:
```bash
cd moblie-app
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
API Documentation: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to Flutter project**:
```bash
cd smart_ocr_scanner
```

2. **Install dependencies**:
```bash
flutter pub get
```

3. **Configure API URL**:

Edit `lib/config/app_config.dart` and set your backend URL:

```dart
// For Android Emulator:
return 'http://10.0.2.2:8000';

// For Real Android Device (use your computer's IP):
return 'http://192.168.1.100:8000';

// For Windows/Desktop:
return 'http://localhost:8000';

// For Production (after deployment):
return 'https://your-app.vercel.app';
```

Find your IP address:
- **Windows**: `ipconfig` → IPv4 Address
- **Mac/Linux**: `ifconfig` or `ip addr`

4. **Run the app**:
```bash
# For connected device or emulator
flutter run

# For specific platform
flutter run -d windows    # Windows
flutter run -d chrome     # Web
flutter run -d android    # Android
```

## 🌐 Deployment

### Deploy Backend to Vercel

1. **Install Vercel CLI**:
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy**:
```bash
vercel --prod
```

4. **Update Flutter App**:
After deployment, update `lib/config/app_config.dart` with your Vercel URL:
```dart
return 'https://your-app.vercel.app';
```

### Deploy Flutter App

#### Android APK
```bash
flutter build apk --release
```
The APK will be at `build/app/outputs/flutter-apk/app-release.apk`

#### iOS (requires macOS)
```bash
flutter build ios --release
```

#### Web
```bash
flutter build web --release
```

## 📡 API Endpoints

### Health Check
```
GET /health
```

### Extract Text from Image
```
POST /extract-text
Content-Type: multipart/form-data

Body:
- file: Image file (JPG, PNG - max 5MB)

Response:
{
  "success": true,
  "data": [
    {
      "text": "Extracted text",
      "confidence": 0.95,
      "bbox": [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
    }
  ]
}
```

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **PaddleOCR**: Ultra-lightweight OCR system by Baidu
- **OpenCV**: Image processing and computer vision
- **Pydantic**: Data validation using Python type annotations

### Frontend
- **Flutter**: Google's UI toolkit for building natively compiled applications
- **Material Design 3**: Modern design system
- **http**: HTTP client for API calls
- **image_picker**: Image selection from camera/gallery
- **shared_preferences**: Local storage for history

## 🔧 Configuration

### Backend Environment Variables
```bash
# Optional: Configure CORS origins
ALLOWED_ORIGINS=["http://localhost:3000", "https://yourdomain.com"]

# Optional: Configure max file size (bytes)
MAX_FILE_SIZE=5242880  # 5MB
```

### Flutter Configuration
Edit `lib/config/app_config.dart`:
- `developmentIP`: Your computer's IP for testing on real devices
- `apiBaseUrl`: Backend API URL (auto-selects based on platform)

## 📝 Development Tips

### Hot Reload (Flutter)
While running the app:
- Press `r` for hot reload
- Press `R` for hot restart
- Press `q` to quit

### Backend Auto-Reload
The backend uses `--reload` flag, so it automatically restarts when you make changes to Python files.

### Debugging
- **Backend**: Check terminal logs for detailed error messages
- **Flutter**: Use Flutter DevTools at `http://localhost:9100`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - OCR engine
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [Flutter](https://flutter.dev/) - UI framework
- [Material Design 3](https://m3.material.io/) - Design system

## 📞 Support

If you have any questions or need help, please open an issue or contact me directly.

## 🚀 Future Enhancements

- [ ] Support for more image formats (PDF, TIFF, etc.)
- [ ] Batch processing multiple images
- [ ] Text translation integration
- [ ] Export to various formats (TXT, PDF, DOCX)
- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] Real-time camera text detection
- [ ] Cloud storage integration

---

⭐ If this project helped you, please give it a star!
