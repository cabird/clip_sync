# Pantry Cloud Integration Plan

## Overview
Add Pantry Cloud as an alternative backend to the existing GitHub Gist implementation, allowing users to choose their preferred storage method.

## Key Design Decisions

### What Pantry Setup Looks Like:
1. User goes to https://getpantry.cloud
2. Enters email address
3. Receives a Pantry ID (UUID format)
4. User pastes this ID into Clipboard Sync app
5. App creates/uses a basket called "clip_sync"
6. Same Pantry ID used on all devices

### What Changes:
- Add backend selection (GitHub vs Pantry)
- Add Pantry ID input field
- Add QR code to share Pantry ID between devices
- Backend abstraction to support both services

### What Stays The Same:
- All existing features work identically
- UI remains familiar
- GitHub users see no changes unless they choose to

## Implementation Phases

### Phase 1: Backend Abstraction
Create a simple backend interface that both GitHub and Pantry can implement:

```javascript
// Pseudo-interface
{
    async testConnection() -> boolean
    async loadHistory() -> array
    async saveHistory(history) -> boolean
    getBackendName() -> string
    getBackendType() -> 'github' | 'pantry'
}
```

### Phase 2: Pantry Implementation
- Use single basket: "clip_sync"
- Same data format as GitHub
- No authentication beyond Pantry ID

### Phase 3: UI Updates
1. Settings modal gets backend selection
2. Show/hide fields based on backend
3. Add "Get Pantry ID" help link
4. Add QR sharing functionality

### Phase 4: QR Code Features
- Generate QR: `PANTRY:${pantryId}`
- Scan QR to auto-fill Pantry ID
- Reuse existing camera permissions

## Technical Details

### Pantry API Endpoints:
```
GET  /apiv1/pantry/{pantryID}/basket/clip_sync
PUT  /apiv1/pantry/{pantryID}/basket/clip_sync
```

### Storage Schema:
```javascript
localStorage.clipboardSyncSettings = {
    backend: 'github' | 'pantry',
    githubToken: '',
    gistId: '',
    pantryId: '',
    autoSync: false,
    syncInterval: 30
}
```

### QR Code Format:
- Pantry: `PANTRY:38e21368-5577-4a1e-b0ba-6ce2077136e1`
- GitHub: `GITHUB:${token}:${gistId}` (if needed)

## UI Flow

### New User:
1. Opens app → Sees backend selection
2. Chooses Pantry → Gets instructions
3. Enters Pantry ID → Connected

### Existing GitHub User:
1. No changes unless they open settings
2. Can switch to Pantry if desired
3. No automatic migration

### Device Pairing:
1. Device A: Settings → Share → QR Code
2. Device B: Settings → Connect → Scan QR
3. Pantry ID auto-filled → Connected

## Benefits
- Easier than GitHub PAT
- No GitHub account needed
- QR codes for easy pairing
- Same features, simpler setup

## Non-Goals
- No data migration between backends
- No complex state management
- No breaking changes
- No over-engineering