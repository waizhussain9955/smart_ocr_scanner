# 🎯 Setup Checklist

## Before Running the App

### ✅ 1. Check Python Installation
```bash
python --version
# Should be 3.10 or higher
```

### ✅ 2. Check Flutter Installation
```bash
flutter doctor
# All checks should pass
```

### ✅ 3. Install Backend Dependencies
```bash
cd d:\protfolio\moblie-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### ✅ 4. Install Flutter Dependencies
```bash
cd smart_ocr_scanner
flutter pub get
```

### ✅ 5. Configure API URL

**Find your IP address:**
```bash
ipconfig
# Look for IPv4 Address (e.g., 192.168.1.55)
```

**Update `smart_ocr_scanner/lib/config/app_config.dart`:**

For Android Phone (on same WiFi):
```dart
static const String developmentIP = 'YOUR_IP_HERE'; // Replace with your IP
return 'http://$developmentIP:8000';
```

For Windows Desktop:
```dart
return 'http://localhost:8000';
```

For Production:
```dart
return 'https://your-app.vercel.app';
```

## 🚀 Running the App

### Option 1: Quick Start (Windows)
Double-click `start.bat` in the project root folder.

### Option 2: Manual Start

**Terminal 1 - Backend:**
```bash
cd d:\protfolio\moblie-app
venv\Scripts\activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Flutter:**
```bash
cd d:\protfolio\moblie-app\smart_ocr_scanner
flutter run
```

## 📱 Testing on Android Phone

1. **Connect phone and computer to same WiFi**

2. **Update IP in app_config.dart** (see step 5 above)

3. **Allow firewall access** when prompted on Windows

4. **Test backend is accessible:**
   - Open browser on your phone
   - Go to: `http://YOUR_IP:8000/health`
   - Should see: `{"status":"healthy"}`

5. **Run the app:**
   ```bash
   flutter run
   ```

## 🧪 Testing Checklist

- [ ] Backend starts without errors
- [ ] Can access http://localhost:8000/docs
- [ ] Health endpoint returns healthy status
- [ ] Flutter app builds successfully
- [ ] Can pick image from camera
- [ ] Can pick image from gallery
- [ ] Image uploads to backend
- [ ] Text extraction works
- [ ] Results display correctly
- [ ] Copy to clipboard works

## 🐛 Common Issues

### "Connection refused" on Android
- ✅ Phone and computer on same WiFi?
- ✅ IP address correct in app_config.dart?
- ✅ Firewall allowing port 8000?
- ✅ Backend server running?

### "Module not found" in Python
- ✅ Virtual environment activated?
- ✅ Dependencies installed? (`pip install -r requirements.txt`)

### Flutter build fails
- ✅ Run `flutter clean`
- ✅ Run `flutter pub get`
- ✅ Run `flutter doctor` and fix any issues

### Images not processing
- ✅ Image size under 5MB?
- ✅ Image format is JPG or PNG?
- ✅ Check backend terminal for errors

## 📦 Building for Production

### Android APK
```bash
cd smart_ocr_scanner
flutter build apk --release
# Output: build/app/outputs/flutter-apk/app-release.apk
```

### Backend Deployment
See `DEPLOYMENT.md` for detailed deployment guide.

## 📚 Documentation

- `README.md` - Complete project documentation
- `DEPLOYMENT.md` - Deployment guide
- `SETUP.md` - This file

## 🆘 Need Help?

1. Check this checklist
2. Review `DEPLOYMENT.md` troubleshooting section
3. Open an issue on GitHub
4. Check backend and Flutter logs for errors

---

✅ Once everything is working, you're ready to deploy to GitHub and Vercel!
