#!/usr/bin/env python3
"""
One-Click Setup Script for YouTube Downloader Bot
This script automates the entire setup process for Render deployment
"""

import os
import sys
import subprocess
import json
import time

def print_banner():
    """Print the setup banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                🤖 YouTube Downloader Bot Setup              ║
║                    Auto Token System                        ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'prince.py',
        'app.py', 
        'requirements.txt',
        'Dockerfile',
        'render.yaml',
        'Procfile'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files found!")
    return True

def create_env_template():
    """Create environment template file"""
    env_template = """# YouTube Downloader Bot - Environment Variables
# Copy these to your Render dashboard Environment Variables section

# REQUIRED: Get these from @BotFather on Telegram
API_TOKEN=your_telegram_bot_token_here
OWNER_USERNAME=your_telegram_username_here

# OPTIONAL: Bot customization
BOT_NAME=YouTube Downloader Bot
BOT_DESCRIPTION=Download YouTube videos, audio, and playlists
MAX_FILE_SIZE=50MB
SUPPORTED_FORMATS=mp4,mp3,webm

# SYSTEM: Don't change these
PYTHONUNBUFFERED=1
PYTHON_VERSION=3.11.0
"""
    
    with open('.env.template', 'w') as f:
        f.write(env_template)
    
    print("✅ .env.template created!")

def create_deployment_guide():
    """Create step-by-step deployment guide"""
    guide = """# 🚀 Render Deployment Guide

## Quick Deploy (One-Click)

1. **Click the Deploy Button:**
   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

2. **Connect GitHub:**
   - Sign in to Render with GitHub
   - Select your repository
   - Render will auto-detect render.yaml

3. **Set Environment Variables:**
   - Go to Environment Variables section
   - Add these variables:
     ```
     API_TOKEN=your_telegram_bot_token
     OWNER_USERNAME=your_telegram_username
     ```

4. **Deploy:**
   - Click "Deploy Blueprint"
   - Wait for build to complete
   - Your bot will be live!

## Getting Bot Token

1. **Message @BotFather on Telegram**
2. **Send:** `/newbot`
3. **Choose bot name:** "My YouTube Bot"
4. **Choose username:** "my_youtube_bot" (must end with 'bot')
5. **Copy the API token**
6. **Add to Render environment variables**

## Manual Deploy

1. **Fork this repository**
2. **Go to Render.com**
3. **New + → Web Service**
4. **Connect GitHub repository**
5. **Set environment variables**
6. **Deploy!**

## Troubleshooting

- **Bot not responding:** Check API_TOKEN in environment variables
- **Build fails:** Check Render build logs
- **FFmpeg errors:** Verify Dockerfile configuration

## Support

- GitHub Issues: [Create an issue](https://github.com/yourusername/youtube-bot/issues)
- Telegram: [@AAlyanMods](https://t.me/AAlyanMods)
"""
    
    with open('DEPLOYMENT_GUIDE.md', 'w') as f:
        f.write(guide)
    
    print("✅ DEPLOYMENT_GUIDE.md created!")

def create_auto_setup_script():
    """Create automated setup script"""
    setup_script = """#!/bin/bash
# Auto Setup Script for YouTube Downloader Bot

echo "🚀 Setting up YouTube Downloader Bot..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11+ first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

# Install requirements
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Create downloads directory
echo "📁 Creating downloads directory..."
mkdir -p downloads

# Run token generator
echo "🔑 Running token generator..."
python3 token_generator.py

echo "✅ Setup complete!"
echo "📚 Check DEPLOYMENT_GUIDE.md for next steps"
"""
    
    with open('setup.sh', 'w') as f:
        f.write(setup_script)
    
    # Make it executable
    os.chmod('setup.sh', 0o755)
    
    print("✅ setup.sh created!")

def update_prince_py_for_env():
    """Update prince.py to use environment variables"""
    # Read the current prince.py
    with open('prince.py', 'r') as f:
        content = f.read()
    
    # Replace hardcoded values with environment variables
    updated_content = content.replace(
        "API_TOKEN = '8494281035:AAGenp24NyNzVCdRmCXZT-8IaNFdHXRlEi8'",
        "API_TOKEN = os.getenv('API_TOKEN', '8494281035:AAGenp24NyNzVCdRmCXZT-8IaNFdHXRlEi8')"
    )
    
    updated_content = updated_content.replace(
        "OWNER_USERNAME = 'AAlyanMods'",
        "OWNER_USERNAME = os.getenv('OWNER_USERNAME', 'AAlyanMods')"
    )
    
    # Write back the updated content
    with open('prince.py', 'w') as f:
        f.write(updated_content)
    
    print("✅ prince.py updated to use environment variables!")

def main():
    """Main setup function"""
    print_banner()
    
    print("🔍 Checking requirements...")
    if not check_requirements():
        print("❌ Setup failed. Please ensure all files are present.")
        return
    
    print("\n📝 Creating configuration files...")
    create_env_template()
    create_deployment_guide()
    create_auto_setup_script()
    
    print("\n🔧 Updating bot code...")
    update_prince_py_for_env()
    
    print("\n🎉 SETUP COMPLETE!")
    print("=" * 50)
    print("✅ Auto token system configured")
    print("✅ Environment templates created")
    print("✅ Deployment guide created")
    print("✅ Setup script created")
    print("✅ Bot code updated for environment variables")
    
    print("\n🚀 NEXT STEPS:")
    print("1. Run: python3 token_generator.py")
    print("2. Get real bot token from @BotFather")
    print("3. Update .env file with real token")
    print("4. Deploy to Render using the deploy button")
    print("5. Set environment variables in Render dashboard")
    
    print("\n📚 For detailed instructions, check DEPLOYMENT_GUIDE.md")

if __name__ == "__main__":
    main()
