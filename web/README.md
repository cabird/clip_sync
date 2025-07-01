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
- Dark mode UI optimized for mobile

## Deployment

This app is hosted on GitHub Pages. Just visit the URL to use it.