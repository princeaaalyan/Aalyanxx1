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

def create_auto_bot():
    """Create automatic bot configuration for Render"""
    print("🤖 Creating auto bot configuration...")
    
    # Generate random bot data
    import random
    import string
    
    bot_names = ['SmartDownloader', 'QuickBot', 'FastHelper', 'SuperDownloader', 'MegaBot', 'UltraHelper']
    bot_name = random.choice(bot_names) + str(random.randint(100, 9999))
    bot_username = bot_name.lower() + "bot"
    
    # Create demo token
    demo_token = "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi"
    
    print(f"📝 Bot Name: {bot_name}")
    print(f"📝 Bot Username: @{bot_username}")
    print(f"🔑 Demo Token: {demo_token}")
    print("⚠️  This is a demo token. Please get a real token from @BotFather")
    
    return {
        'bot_name': bot_name,
        'bot_username': bot_username,
        'token': demo_token
    }

def main():
    """Main entry point for Render deployment"""
    print("🚀 Starting YouTube Downloader Bot on Render...")
    
    # Check FFmpeg
    if not check_ffmpeg():
        print("⚠️  FFmpeg not found, but continuing...")
    
    # Create downloads directory
    os.makedirs("downloads", exist_ok=True)
    print("📁 Downloads directory created")
    
    # Create auto bot configuration
    bot_data = create_auto_bot()
    
    # Set environment variables if not set
    if not os.getenv('API_TOKEN') or os.getenv('API_TOKEN') == 'your_telegram_bot_token_here':
        os.environ['API_TOKEN'] = bot_data['token']
        print(f"🔑 Using demo token: {bot_data['token']}")
    
    if not os.getenv('OWNER_USERNAME') or os.getenv('OWNER_USERNAME') == 'your_telegram_username_here':
        os.environ['OWNER_USERNAME'] = 'AutoUser'
        print("👤 Using default owner: AutoUser")
    
    # Import and run the main bot
    try:
        from prince import bot
        print("🤖 Bot imported successfully")
        print("🔄 Starting bot polling...")
        print("📝 To get real bot token, message @BotFather on Telegram")
        print("📝 Then update API_TOKEN in Render environment variables")
        bot.infinity_polling()
    except Exception as e:
        print(f"❌ Bot error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
