# Clipboard Sync

A simple PWA to sync clipboard content between devices using GitHub Gists as backend.

## Setup

### 1. Get a GitHub Personal Access Token

1. Go to GitHub.com and sign in
2. Click your profile picture → Settings
3. Scroll down to "Developer settings" (at the bottom of the left sidebar)
4. Click "Personal access tokens" → "Tokens (classic)"
5. Click "Generate new token" → "Generate new token (classic)"
6. Give it a name like "Clipboard Sync"
7. Set expiration (or "No expiration" for permanent)
8. Check ONLY the `gist` scope checkbox
9. Click "Generate token" at the bottom
10. **IMPORTANT**: Copy the token immediately - you won't see it again!

### 2. Setup the App

1. Open the app on both devices
2. Enter the same token on both devices
3. The app will automatically find or create a shared gist

## Features

- No server needed - uses GitHub Gists
- Works as a PWA (installable on phones)
- Stores last 20 clipboard items
- Light theme optimized for mobile

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