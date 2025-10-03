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
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ FFmpeg is available")
            return True
        else:
            print("❌ FFmpeg check failed")
            return False
    except Exception as e:
        print(f"❌ FFmpeg error: {e}")
        return False

def main():
    """Main entry point for Render deployment"""
    print("🚀 Starting YouTube Downloader Bot on Render...")
    
    # Check FFmpeg
    if not check_ffmpeg():
        print("⚠️  FFmpeg not found, but continuing...")
    
    # Create downloads directory
    os.makedirs("downloads", exist_ok=True)
    print("📁 Downloads directory created")
    
    # Import and run the main bot
    try:
        from prince import bot
        print("🤖 Bot imported successfully")
        print("🔄 Starting bot polling...")
        bot.infinity_polling()
    except Exception as e:
        print(f"❌ Bot error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
