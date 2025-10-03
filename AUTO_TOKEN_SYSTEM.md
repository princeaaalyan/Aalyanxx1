# 🤖 Auto Token System for Render

## 🚀 **One-Click Deploy with Auto Token Generation**

Your YouTube Downloader Bot now has an **automatic token system** that makes deployment super easy!

## 📁 **New Files Created:**

### 1. **`token_generator.py`** - Interactive Token Setup
- **Guided setup process** for getting bot tokens
- **Step-by-step instructions** for @BotFather
- **Automatic .env file creation**
- **Random username suggestions**

### 2. **`setup.py`** - Complete Auto Setup
- **One-command setup** for entire project
- **Environment variable configuration**
- **Deployment guide generation**
- **Bot code updates for env vars**

### 3. **Updated `render.yaml`** - Auto Token Generation
- **`generateValue: true`** for API_TOKEN and OWNER_USERNAME
- **Pre-configured environment variables**
- **Automatic token generation** during deployment

## 🎯 **How It Works:**

### **Method 1: Automatic Setup (Recommended)**
```bash
# Run the complete setup
python3 setup.py

# This will:
# ✅ Check all requirements
# ✅ Create environment templates
# ✅ Generate deployment guide
# ✅ Update bot code for env vars
# ✅ Create setup scripts
```

### **Method 2: Token Generator Only**
```bash
# Run just the token generator
python3 token_generator.py

# This will:
# ✅ Guide you through @BotFather setup
# ✅ Create .env file
# ✅ Generate random usernames
# ✅ Show step-by-step instructions
```

### **Method 3: Render Auto-Deploy**
1. **Click Deploy Button** → [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
2. **Render automatically generates** API_TOKEN and OWNER_USERNAME
3. **You just need to replace** with real tokens from @BotFather
4. **Deploy!**

## 🔧 **Environment Variables Auto-Configured:**

### **Required (Auto-Generated):**
```yaml
API_TOKEN: generateValue: true
OWNER_USERNAME: generateValue: true
```

### **Optional (Pre-Set):**
```yaml
BOT_NAME: "YouTube Downloader Bot"
BOT_DESCRIPTION: "Download YouTube videos, audio, and playlists"
MAX_FILE_SIZE: "50MB"
SUPPORTED_FORMATS: "mp4,mp3,webm"
PYTHONUNBUFFERED: 1
```

## 🎉 **Benefits of Auto Token System:**

### ✅ **For Users:**
- **No manual configuration** needed
- **Guided setup process** with clear instructions
- **Automatic file generation**
- **One-click deployment**

### ✅ **For Developers:**
- **Consistent deployment** across all users
- **Reduced support requests**
- **Automated environment setup**
- **Easy maintenance**

## 🚀 **Quick Start Guide:**

### **Step 1: Run Setup**
```bash
python3 setup.py
```

### **Step 2: Get Bot Token**
1. Message [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Follow the guided instructions
4. Copy your API token

### **Step 3: Deploy to Render**
1. Click the deploy button
2. Connect your GitHub repository
3. Replace generated tokens with real ones
4. Deploy!

## 📱 **User Experience:**

### **Before (Manual):**
1. Clone repository
2. Install dependencies
3. Get bot token manually
4. Configure environment variables
5. Deploy to platform
6. Set up environment variables again

### **After (Auto):**
1. Click deploy button
2. Replace tokens
3. Deploy!

## 🔍 **Files Structure:**
```
├── prince.py              # Main bot (updated for env vars)
├── app.py                 # Render wrapper
├── token_generator.py     # Interactive token setup
├── setup.py              # Complete auto setup
├── render.yaml           # Auto token generation
├── .env.template         # Environment template
├── DEPLOYMENT_GUIDE.md   # Step-by-step guide
└── setup.sh             # Bash setup script
```

## 🎯 **Next Steps:**

1. **Test the auto setup:**
   ```bash
   python3 setup.py
   ```

2. **Try the token generator:**
   ```bash
   python3 token_generator.py
   ```

3. **Deploy to Render** using the deploy button

4. **Share with users** - they can now deploy with one click!

**Your bot now has a professional auto token system! 🎉✨**
