# ASCII Flappy Bird 🐦 - Pygame

[![Version](https://img.shields.io/badge/Version-1.0-green.svg)]() 

A retro ASCII-style implementation of the classic Flappy Bird game built with Python and Pygame. Features authentic terminal-style graphics with green phosphor aesthetic. Detailed manual compile instructions. Building from source may work on Mac and Linux - 

<img width="794" height="620" alt="Screenshot 2025-12-04 105518" src="https://github.com/user-attachments/assets/a7d0e83e-ed31-4f54-aee5-4695182551f5" />

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

To package the game as a standalone .exe file:

### Quick Method:
```bash
# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller --onefile --windowed --name "FlappyBird_ASCII" flappy_ascii.py
```

---

**Note**: This implementation requires the precompiled wheel file (`pygame-2.6.1-cp311-win_amd64.whl`) due to Windows-specific build requirements. Do not attempt to compile from source on Python 3.12+ as it will fail.
The reccomended way to instal pygame-2.6.1-cp311-win-amd64.whl is pip install --user pygame==2.6.1  ( Installs from PyPI )


<b> Again, Windows users can use the Release .exe in the Releases section, ONLY do this if you trust the source, I recommend reading the code from this repo first.
 </b>

## Attribution

This project is licensed under Apache 2.0. See the [NOTICE](NOTICE) file for 
specific attribution requirements when creating derivative works.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/captainzero)

Version: 0.1 | Author: captainzero93 |

GitHub: https://github.com/captainzero93/
