# Clipboard Sync

A simple PWA to sync clipboard content between devices using Pantry Cloud or GitHub Gists as backend.

## Setup

### Option 1: Pantry Cloud (Easier - Default)

1. **Get a Pantry ID (One-time only)**
   - Go to [getpantry.cloud](https://getpantry.cloud)
   - Enter your email address
   - Name your pantry (anything works - like "my-clipboard" or just your name)
   - Copy the Pantry ID you receive (looks like: 12a34567-8901-2345-b678-9ce0123456e7)
   - **Important:** Save this ID somewhere safe - you only need to get it once, but save it in case your browser storage is cleared!

2. **Setup First Device**
   - Open the app on your first device
   - Click the settings icon (⚙️)
   - Paste your Pantry ID
   - Click "Save & Connect"
   
3. **Add Other Devices - Super Easy!**
   - On your first device: Go to settings and click "Share as QR Code"
   - On new device: Open the app, go to settings, and click "Scan QR Code"
   - That's it! The Pantry ID is automatically filled in

### Option 2: GitHub Gist (Original Method)

1. **Get a GitHub Personal Access Token**
   - Go to GitHub.com and sign in
   - Click your profile picture → Settings
   - Scroll down to "Developer settings" (at the bottom of the left sidebar)
   - Click "Personal access tokens" → "Tokens (classic)"
   - Click "Generate new token" → "Generate new token (classic)"
   - Give it a name like "Clipboard Sync"
   - Set expiration (or "No expiration" for permanent)
   - Check ONLY the `gist` scope checkbox
   - Click "Generate token" at the bottom
   - **IMPORTANT**: Copy the token immediately - you won't see it again!

2. **Setup the App**
   - Open the app on both devices
   - Click settings and change to "GitHub Gist" backend
   - Enter the same token on both devices
   - The app will automatically find or create a shared gist

## Features

- No server needed - uses Pantry Cloud or GitHub Gists
- Works as a PWA (installable on phones and desktops)
- Stores last 20 clipboard items
- Light theme optimized for mobile
- Auto-sync with customizable intervals
- Pin important items to the top
- Delete sensitive items from history
- QR code sharing for easy device pairing (Pantry mode)
- Device type detection (📱 phone or 💻 computer)

## Deployment

### Deploy with GitHub Pages

1. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/clip_sync.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Click on **Settings** (in the repository navigation)
   - Scroll down to **Pages** section (in the left sidebar)
   - Under **Source**, select **Deploy from a branch**
   - Under **Branch**, select **main**
   - Under **Folder**, select **/ (root)**
   - Click **Save**

3. **Access Your App**
   - GitHub will provide a URL like: `https://YOUR_USERNAME.github.io/clip_sync/`
   - The app typically takes 2-10 minutes to become available
   - You can check deployment status in the Actions tab

4. **Install as PWA on Mobile**
   - Visit the GitHub Pages URL on your phone
   - iOS: Tap Share → Add to Home Screen
   - Android: Tap menu → Add to Home Screen

### Custom Domain (Optional)
If you have a custom domain:
1. Add a `CNAME` file in the root directory with your domain
2. Configure your domain's DNS to point to GitHub Pages
3. Enable HTTPS in repository settings