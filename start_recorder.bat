@echo off
echo ================================
echo   Kurmanji Word Recorder
echo   Modern Edition Starting...
echo ================================
echo.

REM Change to the script directory
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Check if required packages are installed
echo Checking dependencies...
python -c "import customtkinter, sounddevice, librosa" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo Dependencies OK!
echo.
echo Starting Kurmanji Word Recorder...
echo.
echo Instructions:
echo 1. Load words from TXT/DOCX/PDF files
echo 2. Check microphone status (should be green)
echo 3. Navigate through words with Previous/Next buttons
echo 4. Record each word by clicking Start Recording
echo 5. Play back to verify, then Save & Next
echo.
echo Press Ctrl+C in this window to close the application
echo.

REM Start the application
python kurmanji_recorder_modern.py

echo.
echo Application closed.
pause