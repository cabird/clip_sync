# Clip Sync

A simple, secure clipboard syncing tool that works across all your devices - no server required!

**Try it now:** [https://www.cabird.com/clip_sync](https://www.cabird.com/clip_sync)

## What is Clip Sync?

Clip Sync lets you easily copy text on one device and paste it on another. Whether you're moving text from your phone to your laptop or vice versa, Clip Sync makes it seamless.

### Key Features

- 📱 **Cross-Platform** - Works on iPhone, Android, Windows, Mac, and Linux
- 🔒 **Secure** - Uses your private GitHub Gist (only you can see your data)
- 🚀 **No Server Needed** - Runs entirely in your browser
- 📌 **Pin Important Items** - Keep frequently used text at the top
- 👁️ **View Full Content** - See complete text with formatting preserved
- 📅 **History** - Stores your last 20 clipboard items
- 🔄 **Auto-Sync** - Automatically checks for new items at customizable intervals
- 🗑️ **Delete Items** - Remove sensitive information from your history
- 💻 **Device Detection** - Shows whether text came from phone (📱) or computer (💻)
- ⚡ **Works Offline** - View your clipboard history even without internet

## How It Works

Clip Sync uses GitHub Gists as a backend to store your clipboard data. This means:
- Your data is stored in your own GitHub account
- Only you can access it (with your personal access token)
- No third-party servers involved
- Completely free (GitHub Gists are free)

## Getting Started

### 1. Get a GitHub Personal Access Token

1. Sign in to [GitHub.com](https://github.com)
2. Click your profile picture → **Settings**
3. Scroll to bottom → **Developer settings**
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token** → **Generate new token (classic)**
6. Name it "Clipboard Sync"
7. Set expiration (or choose "No expiration")
8. Check ONLY the `gist` checkbox
9. Click **Generate token**
10. **Copy the token immediately!** (You won't see it again)

### 2. Set Up Clip Sync

1. Visit [https://www.cabird.com/clip_sync](https://www.cabird.com/clip_sync)
2. Click the settings icon (⚙️)
3. Paste your GitHub token
4. Click "Save & Connect"
5. The app will create a private gist automatically

### 3. Use the Same Token on All Devices

To sync between devices, simply enter the same GitHub token on each device. The app will automatically find your clipboard gist.

## Installation Guide

### Install on iPhone/iPad

1. Open Safari and go to [https://www.cabird.com/clip_sync](https://www.cabird.com/clip_sync)
2. Tap the Share button (square with arrow)
3. Scroll down and tap "Add to Home Screen"
4. Name it "Clip Sync" and tap "Add"
5. The app icon will appear on your home screen

### Install on Android

1. Open Chrome and go to [https://www.cabird.com/clip_sync](https://www.cabird.com/clip_sync)
2. Tap the menu (three dots)
3. Tap "Add to Home screen"
4. Name it "Clip Sync" and tap "Add"
5. The app icon will appear on your home screen

### Install on Windows/Mac/Linux

#### Chrome/Edge:
1. Visit [https://www.cabird.com/clip_sync](https://www.cabird.com/clip_sync)
2. Click the install icon in the address bar (or menu → "Install Clip Sync")
3. Click "Install"
4. The app will open in its own window
5. Pin it to your taskbar/dock for easy access

#### Firefox:
Firefox doesn't support PWA installation, but you can:
1. Bookmark the page
2. Add it to your bookmarks toolbar for quick access

## Using Clip Sync

### Send Text
1. Copy text from any app
2. Open Clip Sync
3. Tap the paste area and paste your text
4. Tap "Send"

### Receive Text
1. Open Clip Sync on your other device
2. The latest text appears automatically
3. Tap "Copy to Clipboard"
4. Paste anywhere you need it

### Features

- **Pin Items**: Click the star (☆) to pin important items to the top
- **View Full**: Click "View" to see the complete text with formatting
- **History**: See your last 20 clipboard items
- **Auto-Sync**: Enable automatic syncing in settings
  - Choose between 15s (fast), 30s (default), or 60s (battery saver)
  - See a blue pulsing indicator when auto-sync is active
  - View the last sync time in settings
- **Delete Items**: Click the red "Delete" button to remove sensitive items
  - Confirmation dialog shows first 50 characters
  - Permanently removes from all devices
- **Manual Refresh**: Click refresh to immediately check for new items

## Privacy & Security

- Your clipboard data is stored in a private GitHub Gist
- Only accessible with your personal access token
- The token is stored locally on your device (never sent anywhere else)
- No third-party can see your clipboard data
- You can revoke access anytime by deleting the token in GitHub

## Tips

- Save your GitHub token in a password manager
- The app works best when installed as a PWA (see installation guides above)
- Pinned items (⭐) stay at the top of your history
- Enable auto-sync for hands-free operation - new items appear automatically
- Use the delete button to remove sensitive information you don't want to keep
- Set auto-sync to 60 seconds on mobile devices to save battery

## Troubleshooting

**Can't see new items?**
- If auto-sync is off, click the Refresh button
- Enable auto-sync in settings for automatic updates
- Make sure you're using the same GitHub token on all devices
- Note: GitHub may cache data for 5-60 seconds

**Installation issues?**
- Clear your browser cache
- Try uninstalling and reinstalling
- Make sure you're using a supported browser

**Token not working?**
- Make sure the token has `gist` permission
- Check that you copied the entire token
- Try generating a new token

## Browser Support

- ✅ Chrome/Edge (Full PWA support)
- ✅ Safari (iOS PWA support)
- ✅ Firefox (No PWA, but fully functional)
- ✅ Most modern mobile browsers

## Open Source

This project is open source! Check out the code at [github.com/cabird/clip_sync](https://github.com/cabird/clip_sync)

---

Made with ❤️ for anyone tired of emailing themselves text