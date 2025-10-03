# YouTube Downloader Telegram Bot

A powerful Telegram bot that can download YouTube videos, shorts, audio (MP3), and entire playlists.

## Features

- 🎬 Download YouTube videos in multiple qualities (144p to 4K)
- 🎞️ Download YouTube Shorts
- 🎵 Extract and download MP3 audio from YouTube videos
- 📃 Download entire YouTube playlists as video or audio
- 🗂️ Automatic file cleanup after sending
- 📊 Real-time download progress updates

## Deploy to Railway

### Method 1: One-Click Deploy
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template-id)

### Method 2: Manual Deploy

1. **Fork this repository** or **create a new Railway project**

2. **Connect your GitHub repository** to Railway

3. **Set Environment Variables** in Railway dashboard:
   ```
   API_TOKEN=your_telegram_bot_token
   OWNER_USERNAME=your_telegram_username
   ```

4. **Deploy** - Railway will automatically:
   - Install dependencies from `requirements.txt`
   - Install FFmpeg (required for audio processing)
   - Start your bot using the `Procfile`

### Getting Your Bot Token

1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow the instructions
3. Copy the API token and add it to Railway environment variables

## Local Development

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install FFmpeg on your system
4. Set your bot token in `prince.py` or use environment variables
5. Run the bot:
   ```bash
   python prince.py
   ```

## Railway Configuration Files

- `requirements.txt` - Python dependencies
- `Procfile` - Tells Railway how to start the app
- `railway.toml` - Railway-specific configuration
- `env.example` - Environment variables template

## Usage

1. Start a chat with your bot
2. Send `/start` to see the main menu
3. Choose your desired download option:
   - **🎬 YT Video** - Download videos with quality selection
   - **🎞️ YT Shorts** - Download YouTube Shorts
   - **🎵 YT MP3** - Extract audio as MP3
   - **📃 Playlist** - Download entire playlists

## Important Notes

- The bot automatically deletes downloaded files after sending them to save storage space
- Railway's free tier has limitations - monitor your usage
- Large files may take time to download and upload
- FFmpeg is automatically installed on Railway for audio processing

## Dependencies

- `pyTelegramBotAPI` - Telegram Bot API wrapper
- `yt-dlp` - YouTube downloader
- `requests` - HTTP library
- `ffmpeg-python` - FFmpeg wrapper (audio processing)

## Support

For issues or questions, contact [@AAlyanMods](https://t.me/AAlyanMods) on Telegram.
