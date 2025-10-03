# 🚀 Render Deployment Guide

## Step-by-Step Render Deployment

### 1. **Prepare Your Code**
✅ All files are ready for Render:
- `prince.py` - Main bot code (with all fixes)
- `app.py` - **NEW** - Render-compatible wrapper
- `requirements.txt` - Python dependencies (updated)
- `Procfile` - Start command
- `Dockerfile` - **NEW** - Docker configuration
- `render.yaml` - **NEW** - Render service config

### 2. **Create GitHub Repository**
```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "YouTube Bot ready for Render deployment"

# Add remote repository (replace with your GitHub repo URL)
git remote add origin https://github.com/yourusername/youtube-bot.git

# Push to GitHub
git push -u origin main
```

### 3. **Deploy to Render**

#### **Method 1: One-Click Deploy (Recommended)**
1. Go to [Render.com](https://render.com)
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure settings (see below)
6. Click "Create Web Service"

#### **Method 2: Using render.yaml**
1. Push code to GitHub
2. In Render dashboard, click "New +" → "Blueprint"
3. Connect your repository
4. Render will auto-detect render.yaml
5. Deploy automatically

### 4. **Render Configuration**

#### **Service Settings:**
- **Name:** `youtube-downloader-bot`
- **Environment:** `Python 3`
- **Region:** `Oregon (US West)` or `Frankfurt (EU)`
- **Branch:** `main`
- **Root Directory:** Leave empty
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`

#### **Environment Variables:**
Add these in Render dashboard:
```
API_TOKEN=your_telegram_bot_token_here
OWNER_USERNAME=your_telegram_username
PYTHONUNBUFFERED=1
```

### 5. **Get Your Bot Token**
1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot`
3. Follow instructions to create bot
4. Copy the API token
5. Add it to Render environment variables

### 6. **Verify Deployment**
1. Check Render logs for any errors
2. Test your bot on Telegram
3. Send `/start` to see if bot responds
4. Try downloading a YouTube video

## 🔧 Configuration Files Explained

### `app.py` (Render Wrapper)
```python
#!/usr/bin/env python3
"""
Render-compatible wrapper for the YouTube Downloader Bot
This file ensures the bot works properly on Render's platform
"""

import os
import sys
import subprocess
import time

def check_ffmpeg():
    """Check if FFmpeg is available"""
    # FFmpeg availability check

def main():
    """Main entry point for Render deployment"""
    # Create downloads directory
    # Import and run the main bot
    from prince import bot
    bot.infinity_polling()
```

### `Dockerfile`
```dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create downloads directory
RUN mkdir -p downloads

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port (Render will set PORT automatically)
EXPOSE 10000

# Start the bot
CMD ["python", "app.py"]
```

### `render.yaml`
```yaml
services:
  - type: web
    name: youtube-downloader-bot
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt && apt-get update && apt-get install -y ffmpeg
    startCommand: python app.py
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: PYTHONUNBUFFERED
        value: 1
```

### `requirements.txt` (Updated)
```
pyTelegramBotAPI==4.14.0
yt-dlp==2025.9.26
requests==2.31.0
ffmpeg-python==0.2.0
gunicorn==21.2.0
```

## 🚨 Important Notes

### Render Free Tier Limits:
- **750 hours** per month
- **Apps sleep** after 15 minutes of inactivity
- **512MB RAM** limit
- **1GB storage** limit

### Bot Features:
- ✅ YouTube video downloads (144p-4K)
- ✅ MP3 audio extraction
- ✅ YouTube Shorts support
- ✅ Playlist downloads
- ✅ Real-time progress updates
- ✅ Auto file cleanup
- ✅ 403 error fixes applied
- ✅ Bot detection bypass

### Security:
- ✅ Bot token in environment variables
- ✅ No sensitive data in code
- ✅ Proper error handling

## 🐛 Troubleshooting

### Common Issues:
1. **Bot not responding**: Check API_TOKEN in environment variables
2. **FFmpeg errors**: Verify Dockerfile FFmpeg installation
3. **Build failures**: Check Render build logs
4. **Memory issues**: Monitor Render usage dashboard

### Render Logs:
- Go to your service dashboard
- Click "Logs" tab
- Check for any error messages
- Look for "✅ FFmpeg is available" message

### Support:
- Render Documentation: [render.com/docs](https://render.com/docs)
- Bot Issues: Check Telegram bot logs in Render dashboard

## 🎉 Success!
Your YouTube Downloader Bot is now running 24/7 on Render! 🚀

## 📁 **Current File Structure:**
```
├── prince.py              # Main bot code
├── app.py                 # Render wrapper
├── requirements.txt       # Python dependencies  
├── Procfile              # Start command
├── Dockerfile            # Docker configuration
├── render.yaml           # Render service config
├── README.md            # Documentation
├── RENDER_DEPLOY.md     # This guide
└── env.example          # Environment variables template
```

**Ab Render pe deploy karo - sab kuch ready hai! 🎵✨**
