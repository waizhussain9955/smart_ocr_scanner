# 🚀 Backend Deployment Guide

## Option 1: Railway.app (RECOMMENDED for PaddleOCR)

### Why Railway?
- ✅ Supports large ML models (PaddleOCR ~500MB)
- ✅ No size limitations like Vercel
- ✅ Perfect for FastAPI + Python
- ✅ Free tier: $5 credit/month
- ✅ Easy GitHub integration

### Steps:

1. **Go to**: https://railway.app

2. **Sign Up** with GitHub account

3. **Click**: "New Project" → "Deploy from GitHub repo"

4. **Select Repository**: `waizhussain9955/smart_ocr_scanner`

5. **Railway will auto-detect** it's a Python project

6. **Configure** (if needed):
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

7. **Add Environment Variables** (optional):
   - `PYTHON_VERSION`: `3.10`

8. **Click**: "Deploy"

9. **Get Your URL**:
   - After deployment, click on your service
   - Go to "Settings" → "Networking"
   - Click "Generate Domain"
   - You'll get: `https://smart-ocr-scanner-production.up.railway.app`

10. **Test Your Backend**:
    ```
    https://your-railway-url.up.railway.app/health
    https://your-railway-url.up.railway.app/docs
    ```

11. **Update Flutter App**:
    Edit `smart_ocr_scanner/lib/config/app_config.dart`:
    ```dart
    return 'https://your-railway-url.up.railway.app';
    ```

---

## Option 2: Render.com

### Steps:

1. **Go to**: https://render.com

2. **Sign Up** with GitHub

3. **Click**: "New" → "Web Service"

4. **Connect Repository**: `smart_ocr_scanner`

5. **Configure**:
   - **Name**: `smart-ocr-backend`
   - **Region**: Choose nearest to you
   - **Branch**: `main`
   - **Root Directory**: Leave empty
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

6. **Click**: "Create Web Service"

7. **Wait for deployment** (first time takes 5-10 minutes due to PaddleOCR download)

8. **Get URL**: `https://smart-ocr-backend.onrender.com`

9. **Test**: `https://your-url.onrender.com/health`

---

## Option 3: Vercel (Current - But Not Recommended for ML)

Your backend is already deployed but has routing issues. Vercel is not ideal for FastAPI + ML models.

Current URL: `https://smart-ocr-scanner.vercel.app`

### If you want to fix Vercel:

The issue is Vercel expects serverless functions, not a full FastAPI app. You would need to:
1. Convert to serverless format
2. Reduce package size
3. Handle cold starts

**Not recommended** for PaddleOCR.

---

## Option 4: DigitalOcean App Platform

### Steps:

1. **Go to**: https://digitalocean.com

2. **Sign Up** (get $200 free credit for 60 days)

3. **Create App** → Connect GitHub

4. **Select**: `smart_ocr_scanner` repository

5. **Configure**:
   - **Source**: GitHub
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

6. **Deploy**

7. **Cost**: ~$5-12/month

---

## ✅ Recommended: Railway.app

**Railway is the best choice because:**
- ✅ Easiest setup
- ✅ Works perfectly with PaddleOCR
- ✅ No configuration headaches
- ✅ Free tier available
- ✅ Auto-deploys on git push

---

## After Deployment:

### 1. Test Backend:
```bash
# Test health endpoint
curl https://your-backend-url.com/health

# Expected: {"status":"healthy"}

# Test API docs
Open: https://your-backend-url.com/docs
```

### 2. Update Flutter App:
```dart
// File: smart_ocr_scanner/lib/config/app_config.dart
return 'https://your-backend-url.com';
```

### 3. Build APK:
```bash
cd smart_ocr_scanner
flutter build apk --release
```

### 4. Install APK on Phone
- Transfer APK to phone
- Install (enable "Unknown Sources")
- Start scanning! 🎉

---

## Need Help?

Check logs:
- **Railway**: Dashboard → Logs
- **Render**: Dashboard → Logs
- **Vercel**: Dashboard → Functions

Common Issues:
- **Port error**: Make sure to use `$PORT` environment variable
- **Dependencies**: Check `requirements.txt` has all packages
- **Size**: PaddleOCR is large, Railway/Render handle it better

---

**Good luck with deployment! 🚀**
