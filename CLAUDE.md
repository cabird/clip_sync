# Cross-Copy-Paste Project Instructions

## IMPORTANT: Version Updates

**ALWAYS increment the version number when making ANY commits to the web app.**

Version number locations to update:
1. `/web/index.html` - Line ~366 in the header span
2. `/web/sw.js` - Line 2 in CACHE_NAME constant

Version numbering scheme:
- **Patch** (1.0.X) - Bug fixes, style changes, minor updates
- **Minor** (1.X.0) - New features, significant improvements
- **Major** (X.0.0) - Breaking changes, major refactors

Current version: **v1.1.0**

## Project Structure

```
cross-copy-paste/
├── web/                    # PWA (Progressive Web App)
│   ├── index.html         # Main app - single file contains all code
│   ├── manifest.json      # PWA manifest
│   ├── sw.js             # Service worker for offline support
│   ├── icon.svg          # App icon (SVG)
│   ├── apple-touch-icon.png  # iOS home screen icon
│   └── README.md         # Deployment instructions
├── index.html            # Root redirect to /web/
└── windows/              # (Future) Windows tray app
```

## Key Information

### GitHub Pages Deployment
- Hosted at: https://www.cabird.com/cross-copy-paste/web/
- Deployed from main branch, root directory
- Uses redirect from root to /web/ subdirectory

### PWA Considerations
- The app is served from a subdirectory, not root
- Manifest uses absolute paths: `/cross-copy-paste/web/`
- Service worker uses relative paths for caching
- Both iOS and Windows PWA installations tested

### Technology Stack
- Pure HTML/CSS/JavaScript (no build process)
- GitHub Gists as backend (no server needed)
- GitHub Personal Access Token for authentication
- PWA features for mobile/desktop installation

### Color Scheme
- Light theme (changed from dark)
- Primary color: #2196F3 (blue)
- Background: #f5f5f5
- Cards: #ffffff with shadows

### Testing Checklist
When making changes:
1. Test on mobile browser
2. Test PWA installation (iOS/Android)
3. Test on desktop browser
4. Test PWA installation (Windows/Mac)
5. Verify clipboard operations work
6. Check that version number is visible

### Common Tasks

#### Adding new features
1. Update version number (minor increment)
2. Test thoroughly on mobile and desktop
3. Update README if needed
4. Commit with descriptive message

#### Fixing bugs
1. Update version number (patch increment)
2. Test the specific fix
3. Verify no regressions
4. Commit with "Fix: [description]" message

#### Style changes
1. Update version number (patch increment)
2. Maintain light theme consistency
3. Test on various screen sizes
4. Commit changes

### Browser Cache Issues
Users may need to:
- Force refresh (Ctrl+F5)
- Uninstall/reinstall PWA
- Clear browser cache
The version number helps identify cache issues.

## Future Enhancements Discussed
- Windows system tray app (Electron)
- Auto-sync without manual refresh
- Encryption options
- Multiple clipboard support
- Search functionality for history

## Remember
- This is a simple, user-friendly tool
- No user accounts or complex setup
- One GitHub token works for all devices
- Keep the UI clean and minimal