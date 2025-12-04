# ASCII Flappy Bird 🐦 - Pygame

[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)]() 

check out Pygame Snake here: https://github.com/captainzero93/simple-snake-python-pygme

check out Pygame ANSCII Tetris here: https://github.com/captainzero93/Anscii-Tetris-PYGAME

<img width="794" height="620" alt="Screenshot 2025-12-04 105518" src="https://github.com/user-attachments/assets/feea82ef-a704-4a5a-99bd-e7d1a16ebf95" />


A retro ASCII-style implementation of the classic Flappy Bird game built with Python and Pygame. Features authentic terminal-style graphics with green phosphor aesthetic. Detailed manual compile instructions. Building from source may work on Mac and Linux - added a beta .PKG build for Linux (untested). 

## Features
- Classic flappy bird mechanics: navigate through pipes!
- Retro ASCII graphics with green terminal aesthetic
- Simple spacebar controls for flapping
- Score tracking system
- Game over when hitting pipes, ceiling, or ground
- Clean UI with ASCII art bird and pipe obstacles
- Smooth physics with gravity simulation

## Requirements
- **Python 3.11** (required for precompiled wheel compatibility)
- Pygame (`pygame==2.6.1`)
- all other requirments are in the requirments.txt even if they are not needed

 ## Compiled setup - Windows users can use the Release .exe in the Releases section, ONLY do this if you trust the source, I recommend reading the code from this repo first. Refer to the documentatiom for your Linux Distro for unzipping and instaling the beta Linux .PKG zip / file.
  
## Manual installation & Setup
### Step 1: Create Virtual Environment / Clone repo

<b> Download and extract this repo, Install Python 11 - ensire you check 'Add to path in the installer. Open CMD from the extracted folder; </b>

```bash
python -m venv flappy_venv

or Create venv using Python 3.11 explicitly:

python -m venv flappy_venv --system-site-packages

```

### Step 2: Activate Virtual Environment
```powershell
# Windows (PowerShell):
.\flappy_venv\Scripts\activate.ps1

```

### Step 3: Install Dependencies
```bash

pip install -r requirements.txt

or

pip install --user pygame==2.6.1  # Install from PyPI ( recommended ) 


or

pip install --user  "folder_with_pygame.whl package\pygame-2.6.1-cp311-win_amd64.whl"  # Replace with real path.
```

> ⚠️ **Important**: The wheel file requires Python 3.11. If you're using a different version, download the correct wheel or install from source.

## Running the Game
```bash
From inside the folder flappy_ascii.py exists;

python flappy_ascii.py

```
Or download the self contained Windows ( or beta Linux .PKG) build in Releases. ( Only do this if you trust the source).

### Controls
| Key | Action |
|-----|--------|
| SPACE  | Flap / Start Game / Restart |
| ESC  | Quit Game |

<b> RULES: </b> You are the ASCII bird ( >o) ), navigate through the pipe gaps by pressing SPACE to flap. Do NOT hit the pipes, ceiling, or ground!

## Project Structure
```
Extracted_files/
├── README.md                # This file
├── flappy_ascii.py          # Main game logic
├── build_exe.bat            # Windows build script for creating .exe
├── build_exe.sh             # Linux/Mac build script
├── PACKAGING_README.md      # Detailed packaging instructions
├── QUICK_REFERENCE.txt      # Quick packaging guide
├── LICENSE                  # Auto-generated Apache 2.0 License
├── NOTICE                   # Apache 2.0 compatible attribution notice
├── requirements.txt         # Requirements file for building
├── .gitignore               # Allows release files over 25 mb
     
```

## Technical Details
- Built using **Python 3.11** for compatibility with pygame
- Uses physics-based movement with gravity and flapping mechanics
- Score increases by one point for each pipe successfully passed
- Game ends when bird collides with pipes, ceiling, or ground
- Retro ASCII aesthetic with green phosphor terminal colors
- Bird sprite: `>o)` and `(_>` characters
- Pipes rendered with `║` characters
- Clean, readable code with modular class structure

## Building Single-File Executable

### Windows .exe
To build on Windows:
```bash
# Automated
build_exe.bat

# OR Manual
pip install pyinstaller
pyinstaller --onefile --windowed --name "FlappyBird_ASCII" flappy_ascii.py
```
Output: `dist/FlappyBird_ASCII.exe`

### Linux Binary + Package
To build on Linux:
```bash
# Automated (creates binary + .tar.gz)
./build_exe.sh

# Output:
#   dist/FlappyBird_ASCII (binary)
#   FlappyBird_ASCII_Linux.tar.gz (distributable)
```

### Arch Linux Package (.pkg)
To build on Arch Linux:
```bash
./build_arch_pkg.sh

# Creates: flappybird-ascii-1.0-1-x86_64.pkg.tar.zst
# Install: sudo pacman -U flappybird-ascii-*.pkg.tar.zst
```

### Docker (Build Linux from Windows)
If you want to build Linux version from Windows:
```bash
# Build using Docker
build_linux_docker.bat

# OR manually:
docker build -t flappybird-builder .
docker run -v "%cd%":/app flappybird-builder
```

### Important: Cross-Platform Limitations
⚠️ **PyInstaller cannot cross-compile!**
- Windows builds only work on Windows
- Linux builds only work on Linux
- You must build on each target platform

See `CROSSPLATFORM_BUILD.md` for detailed multi-platform build instructions, including GitHub Actions automation.

---

**Note**: This implementation requires the precompiled wheel file (`pygame-2.6.1-cp311-win_amd64.whl`) due to Windows-specific build requirements. Do not attempt to compile from source on Python 3.12+ as it will fail.
The reccomended way to instal pygame-2.6.1-cp311-win-amd64.whl is pip install --user pygame==2.6.1  ( Installs from PyPI )


<b> Again, Windows users can use the Release .exe in the Releases section, ONLY do this if you trust the source, I recommend reading the code from this repo first.
Refer to the documentatiom for your Linux Distro for unzipping and instaling the .PKG zip / file. </b>

## Attribution

This project is licensed under Apache 2.0. See the [NOTICE](NOTICE) file for 
specific attribution requirements when creating derivative works.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/captainzero)

Version: 1.0 | Author: captainzero93 |

GitHub: https://github.com/captainzero93/




GitHub: https://github.com/captainzero93/
