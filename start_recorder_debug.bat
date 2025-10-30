@echo off
echo =======================================
echo   Kurmanji Word Recorder - Debug Mode
echo =======================================
echo.

cd /d "%~dp0"

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found
    pause
    exit /b 1
)

echo Python: OK
echo Dependencies: Checking...

python -c "import customtkinter, sounddevice, librosa, soundfile" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    python -m pip install -r requirements.txt
)

echo Dependencies: OK
echo.

REM Create directories if they don't exist
if not exist "kurmanji_dataset" mkdir kurmanji_dataset
if not exist "kurmanji_dataset\audio" mkdir kurmanji_dataset\audio
if not exist "kurmanji_dataset\documents" mkdir kurmanji_dataset\documents

echo Directories: OK
echo.

REM Test audio system quickly
echo Testing audio system...
python -c "import sounddevice; print('Audio devices:', len([d for d in sounddevice.query_devices() if d['max_input_channels'] > 0]))" 2>&1

echo.
echo Starting application with debug output...
echo If you encounter issues, check the output below:
echo ----------------------------------------
echo.

REM Start with debug output
python kurmanji_recorder_modern.py

echo.
echo ----------------------------------------
echo Application closed.
echo.
echo If there were errors, please check:
echo 1. Microphone permissions in Windows Settings
echo 2. Antivirus software blocking file access  
echo 3. Available disk space
echo 4. File permissions in the kurmanji folder
echo.
pause