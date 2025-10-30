# Kurmanji Recorder - Build Instructions

## Building Executables

### Prerequisites
Install PyInstaller:
```bash
pip install pyinstaller
```

---

## Windows Build

### On Windows:
```powershell
cd c:\Users\PyxSara\Desktop\kurmanji
pyinstaller build_windows.spec
```

**Output:** `dist/KurmanjiRecorder/KurmanjiRecorder.exe`

**To distribute:**
1. Zip the entire `dist/KurmanjiRecorder/` folder
2. Users extract and run `KurmanjiRecorder.exe`

---

## macOS Build (Intel & M1/M2/M3)

### Option 1: Build on Mac (Recommended)
You need access to a Mac to build the macOS version.

**On macOS (Intel or Apple Silicon):**
```bash
# Install dependencies
pip install pyinstaller

# Build the app
pyinstaller build_macos.spec
```

**Output:** `dist/KurmanjiRecorder.app`

**Universal Binary (both Intel & Apple Silicon):**
```bash
# Build on Apple Silicon Mac for universal binary
pyinstaller build_macos.spec --target-arch universal2
```

---

### Option 2: GitHub Actions (Build remotely - FREE)

If you don't have a Mac, use GitHub Actions to build automatically:

1. Create a GitHub repository
2. Push your code
3. GitHub Actions will build Windows + macOS versions
4. Download the executables from GitHub Releases

I can create the GitHub Actions workflow file for you if you want this option.

---

## File Size Optimization

The executable will be large (~150-300MB) due to Python + libraries. To reduce:

```bash
# Use --onefile for single executable (slower startup)
pyinstaller --onefile --windowed kurmanji_recorder_clean.py

# Or use UPX compression (already enabled in .spec files)
```

---

## Testing

**Windows:**
```powershell
.\dist\KurmanjiRecorder\KurmanjiRecorder.exe
```

**macOS:**
```bash
open dist/KurmanjiRecorder.app
```

---

## Code Signing (Optional but Recommended)

### Windows:
- Users need to sign with a code signing certificate
- Without signing, Windows Defender may show warnings

### macOS:
- Requires Apple Developer account ($99/year)
- Without signing, users must right-click → Open (bypass Gatekeeper)

```bash
# macOS signing (if you have certificate)
codesign --deep --force --sign "Developer ID Application: Your Name" dist/KurmanjiRecorder.app
```

---

## Quick Start

**Just want to try on Windows now?**
```powershell
pip install pyinstaller
pyinstaller build_windows.spec
```

Then run: `dist\KurmanjiRecorder\KurmanjiRecorder.exe`
