#!/usr/bin/env python3
"""
Auto Token Generator for YouTube Downloader Bot
This script helps users automatically generate and configure bot tokens
"""

import os
import sys
import requests
import json
import time
import random
import string

def generate_random_username():
    """Generate a random username for the bot"""
    adjectives = ['Smart', 'Quick', 'Fast', 'Super', 'Mega', 'Ultra', 'Pro', 'Elite', 'Prime', 'Max']
    nouns = ['Bot', 'Downloader', 'Helper', 'Assistant', 'Manager', 'Tool', 'Service', 'App']
    
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(100, 9999)
    
    return f"{adj}{noun}{number}"

def generate_bot_token():
    """Generate a mock bot token for demonstration"""
    # This is a mock token - users need to get real token from @BotFather
    return "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi"

def create_env_file(api_token, owner_username):
    """Create .env file with the provided tokens"""
    env_content = f"""# YouTube Downloader Bot Environment Variables
# Generated automatically by token_generator.py

# Telegram Bot Configuration
API_TOKEN={api_token}
OWNER_USERNAME={owner_username}

# Bot Settings
PYTHONUNBUFFERED=1
BOT_NAME=YouTube Downloader Bot
BOT_DESCRIPTION=Download YouTube videos, audio, and playlists

# Optional: Customize these if needed
MAX_FILE_SIZE=50MB
SUPPORTED_FORMATS=mp4,mp3,webm
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ .env file created successfully!")

def display_instructions():
    """Display step-by-step instructions for getting real token"""
    print("\n" + "="*60)
    print("🤖 BOT TOKEN SETUP INSTRUCTIONS")
    print("="*60)
    print("\n1. Open Telegram and search for @BotFather")
    print("2. Send /newbot command")
    print("3. Choose a name for your bot (e.g., 'My YouTube Bot')")
    print("4. Choose a username (must end with 'bot', e.g., 'my_youtube_bot')")
    print("5. Copy the API token you receive")
    print("6. Replace the API_TOKEN in .env file with your real token")
    print("\n" + "="*60)
    print("📝 EXAMPLE CONVERSATION WITH @BotFather:")
    print("="*60)
    print("You: /newbot")
    print("BotFather: Alright, a new bot. How are we going to call it?")
    print("You: My YouTube Downloader Bot")
    print("BotFather: Good. Now let's choose a username for your bot.")
    print("You: my_youtube_downloader_bot")
    print("BotFather: Done! Here's your token: 1234567890:ABC...")
    print("="*60)

def create_render_env_template():
    """Create Render environment variables template"""
    render_env = """# Render Environment Variables Template
# Copy these to your Render dashboard Environment Variables section

API_TOKEN=your_telegram_bot_token_here
OWNER_USERNAME=your_telegram_username_here
PYTHONUNBUFFERED=1
BOT_NAME=YouTube Downloader Bot
BOT_DESCRIPTION=Download YouTube videos, audio, and playlists
MAX_FILE_SIZE=50MB
SUPPORTED_FORMATS=mp4,mp3,webm
"""
    
    with open('render.env.template', 'w') as f:
        f.write(render_env)
    
    print("✅ render.env.template created!")

def main():
    """Main function to run the token generator"""
    print("🚀 YouTube Downloader Bot - Auto Token Generator")
    print("=" * 50)
    
    # Generate random username
    suggested_username = generate_random_username()
    print(f"📝 Suggested bot username: @{suggested_username}")
    
    # Get user input
    print("\n🔧 CONFIGURATION SETUP")
    print("-" * 30)
    
    # Get API token
    api_token = input(f"Enter your Telegram Bot API Token (or press Enter for demo): ").strip()
    if not api_token:
        api_token = generate_bot_token()
        print(f"⚠️  Using demo token: {api_token}")
        print("   (You need to replace this with a real token from @BotFather)")
    
    # Get owner username
    owner_username = input(f"Enter your Telegram username (without @): ").strip()
    if not owner_username:
        owner_username = "your_username"
        print(f"⚠️  Using placeholder: {owner_username}")
    
    # Create files
    print("\n📁 CREATING CONFIGURATION FILES...")
    print("-" * 40)
    
    create_env_file(api_token, owner_username)
    create_render_env_template()
    
    # Display instructions
    display_instructions()
    
    print("\n🎉 SETUP COMPLETE!")
    print("=" * 30)
    print("✅ .env file created")
    print("✅ render.env.template created")
    print("✅ Ready for deployment!")
    
    print("\n🚀 NEXT STEPS:")
    print("1. Get real bot token from @BotFather")
    print("2. Update .env file with real token")
    print("3. Deploy to Render using the deploy button")
    print("4. Set environment variables in Render dashboard")
    
    print("\n📚 For detailed instructions, check README.md")

if __name__ == "__main__":
    main()
