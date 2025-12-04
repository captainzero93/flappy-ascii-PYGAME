# ASCII Tetris 🎮 - Pygame

[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)]() 

A retro ASCII-style implementation of the classic Tetris game built with Python and Pygame. Features clean terminal-style graphics with colorful block aesthetics and authentic Tetris mechanics. Detailed manual compile instructions. Building from source may work on Mac and Linux - 

check out Pygame Snake here: https://github.com/captainzero93/simple-snake-python-pygme
check out Pygame ANSCII Flappy Bird here: https://github.com/captainzero93/flappy-ascii-PYGAME

[Screenshot placeholder - Add your game screenshot here]

## Features
- Classic Tetris mechanics with all 7 tetromino shapes (I, O, T, S, Z, J, L)
- Ghost piece preview showing landing position
- Retro ASCII graphics with colored block aesthetic
- Intuitive arrow key and space bar controls
- Progressive difficulty system - speed increases with level
- Line clearing with score multipliers (1-4 lines)
- Next piece preview system
- Wall kick rotation mechanics
- Score tracking, lines cleared, and level progression
- Smooth piece movement with gravity simulation
- Game over detection with restart capability

## Requirements
- **Python 3.11** (required for precompiled wheel compatibility)
- Pygame (`pygame==2.6.1`)
- all other requirements are in the requirements.txt even if they are not needed

## Compiled setup - Windows users can use the Release .exe in the Releases section, ONLY do this if you trust the source, I recommend reading the code from this repo first. Refer to the documentation for your Linux Distro for unzipping and installing the beta Linux .PKG zip / file.
  
## Manual installation & Setup
### Step 1: Create Virtual Environment / Clone repo

<b> Download and extract this repo, Install Python 11 - ensure you check 'Add to path' in the installer. Open CMD from the extracted folder; </b>

```bash
python -m venv tetris_venv

or Create venv using Python 3.11 explicitly:

python -m venv tetris_venv --system-site-packages

```

### Step 2: Activate Virtual Environment
```powershell
# Windows (PowerShell):
.\tetris_venv\Scripts\activate.ps1

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
From inside the folder tetris.py exists;

python tetris.py

```
Or download the self contained Windows ( or beta Linux .PKG) build in Releases. ( Only do this if you trust the source).

### Controls
| Key | Action |
|-----|--------|
| ← →  | Move piece left/right |
| ↑  | Rotate piece clockwise |
| ↓  | Soft drop (faster falling) |
| SPACE  | Hard drop (instant placement) |
| R  | Restart game (after game over) |
| ESC  | Quit Game |

<b> RULES: </b> Rotate and position falling tetromino pieces to create complete horizontal lines. Each completed line clears and awards points. The game ends when pieces stack to the top of the playfield!

## Technical Details
- Built using **Python 3.11** for compatibility with pygame
- Uses physics-based falling mechanics with progressive speed increase
- Score system: 100/300/500/800 points for 1/2/3/4 lines cleared (multiplied by level)
- Level increases every 10 lines cleared
- Fall speed accelerates with each level (minimum 100ms delay)
- All 7 classic tetromino shapes with authentic colors
- Ghost piece shows exact landing position
- Wall kick system for improved rotation mechanics
- Clean, modular code with separate Tetromino and TetrisGame classes
- 10x20 playfield grid matching classic Tetris dimensions
- Next piece preview in sidebar
- Real-time statistics display (score, lines, level)

## Building Single-File Executable

To package the game as a standalone .exe file:

### Quick Method:
```bash
# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller --onefile --windowed --name "Tetris_ASCII" tetris.py
```

---

## Game Mechanics

### Scoring System
- **Single Line**: 100 × Level
- **Double Lines**: 300 × Level  
- **Triple Lines**: 500 × Level
- **Tetris (4 Lines)**: 800 × Level
- **Soft Drop**: +1 point per cell
- **Hard Drop**: +2 points per cell

### Level Progression
- Start at Level 1
- Level increases every 10 lines cleared
- Fall speed decreases by 50ms per level
- Minimum fall speed: 100ms (Level 9+)

---

**Note**: This implementation requires the precompiled wheel file (`pygame-2.6.1-cp311-win_amd64.whl`) due to Windows-specific build requirements. Do not attempt to compile from source on Python 3.12+ as it will fail.
The recommended way to install pygame-2.6.1-cp311-win-amd64.whl is pip install --user pygame==2.6.1  ( Installs from PyPI )


<b> Again, Windows users can use the Release .exe in the Releases section, ONLY do this if you trust the source, I recommend reading the code from this repo first.
 </b>

## Attribution

This project is licensed under Apache 2.0. See the [NOTICE](NOTICE) file for 
specific attribution requirements when creating derivative works.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/captainzero)

Version: 1.0 | Author: captainzero93 |

GitHub: https://github.com/captainzero93/
