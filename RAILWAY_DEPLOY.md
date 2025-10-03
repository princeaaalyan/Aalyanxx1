# 🚀 Railway Deployment Guide

## Step-by-Step Railway Deployment

### 1. **Prepare Your Code**
✅ All files are ready:
- `prince.py` - Main bot code (with 403 error fixes)
- `requirements.txt` - Python dependencies
- `Procfile` - Railway start command
- `railway.toml` - Railway configuration
- `nixpacks.toml` - Build configuration
- `README.md` - Documentation

### 2. **Create GitHub Repository**
```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit - YouTube Downloader Bot"

# Add remote repository (replace with your GitHub repo URL)
git remote add origin https://github.com/yourusername/youtube-bot.git

# Push to GitHub
git push -u origin main
```

### 3. **Deploy to Railway**

#### Option A: One-Click Deploy
1. Go to [Railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will automatically detect and deploy

#### Option B: Railway CLI
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Deploy
railway up
```

### 4. **Set Environment Variables**
In Railway Dashboard:
1. Go to your project
2. Click "Variables" tab
3. Add these variables:
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
5. Add it to Railway environment variables

### 6. **Verify Deployment**
1. Check Railway logs for any errors
2. Test your bot on Telegram
3. Send `/start` to see if bot responds
4. Try downloading a YouTube video

## 🔧 Configuration Files Explained

### `requirements.txt`
```
pyTelegramBotAPI==4.14.0  # Telegram bot framework
yt-dlp==2025.9.26         # Latest YouTube downloader
requests==2.31.0          # HTTP requests
ffmpeg-python==0.2.0      # Audio processing
```

### `railway.toml`
```toml
[build]
builder = "NIXPACKS"      # Use Nixpacks for building

[deploy]
startCommand = "python prince.py"    # Start command
restartPolicyType = "ON_FAILURE"     # Auto-restart on failure
restartPolicyMaxRetries = 10         # Max restart attempts

[variables]
PYTHONUNBUFFERED = "1"    # Show Python output in logs
```

### `nixpacks.toml`
```toml
[phases.setup]
nixPkgs = ["python3", "ffmpeg"]      # Install Python and FFmpeg

[phases.install]
cmds = ["pip install -r requirements.txt"]  # Install dependencies

[phases.build]
cmds = ["mkdir -p downloads"]        # Create downloads directory

[start]
cmd = "python prince.py"             # Start the bot
```

## 🚨 Important Notes

### Railway Free Tier Limits:
- **$5 free credit** per month
- **500MB RAM** limit
- **1GB storage** limit
- **Apps sleep** after 30 minutes of inactivity

### Bot Features:
- ✅ YouTube video downloads (144p-4K)
- ✅ MP3 audio extraction
- ✅ YouTube Shorts support
- ✅ Playlist downloads
- ✅ Real-time progress updates
- ✅ Auto file cleanup
- ✅ 403 error fixes applied

### Security:
- ✅ Bot token in environment variables
- ✅ No sensitive data in code
- ✅ Proper error handling

## 🐛 Troubleshooting

### Common Issues:
1. **Bot not responding**: Check API_TOKEN in environment variables
2. **Download errors**: Verify FFmpeg is installed (handled by nixpacks.toml)
3. **Memory issues**: Monitor Railway usage dashboard
4. **Build failures**: Check Railway build logs

### Support:
- Railway Documentation: [docs.railway.app](https://docs.railway.app)
- Bot Issues: Check Telegram bot logs in Railway dashboard

## 🎉 Success!
Your YouTube Downloader Bot is now running 24/7 on Railway! 🚀
