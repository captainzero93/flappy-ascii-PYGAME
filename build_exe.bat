@echo off
echo ================================
echo  ASCII Flappy Bird - EXE Builder
echo ================================
echo.

REM Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
    echo.
)

echo Building single-file executable...
echo.

REM Build the executable
pyinstaller --onefile --windowed --name "FlappyBird_ASCII" --icon=NONE flappy_ascii.py

echo.
echo ================================
echo Build complete!
echo ================================
echo.
echo Your executable is located at:
echo dist\FlappyBird_ASCII.exe
echo.
echo You can distribute this single file to anyone!
echo.
pause
