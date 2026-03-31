# Translator App

Современный артиллерийский словарь с автопереводом и подсказками.

## Features

- Automatic translation while typing
- Word suggestions (up to 5 similar words)
- Excel dictionary support with merged cells
- Fast search with prefix and fuzzy matching
- Cross-platform (Windows, macOS, Linux)

## Quick Start

### Windows
Download [TranslatorApp.exe](dist/TranslatorApp.exe) and double-click to run.

### macOS / Linux
Build from source (see instructions below).

## Build from Source

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Steps
```bash
# Clone repository
git clone https://github.com/merc11less-dev/translator_app.git
cd translator_app

# Install dependencies
pip install -r requirements.txt

# Run directly (without building)
python main.py

# Or build executable
# Windows:
pyinstaller --onefile --windowed --name "TranslatorApp" --add-data "sources/words.xlsx;sources" main.py

# macOS:
pyinstaller --onefile --windowed --name "TranslatorApp" --add-data "sources/words.xlsx:sources" main.py

# Linux:
pyinstaller --onefile --name "TranslatorApp" --add-data "sources/words.xlsx:sources" main.py

# Run built executable
# Windows:
dist\TranslatorApp.exe
# macOS/Linux:
./dist/TranslatorApp