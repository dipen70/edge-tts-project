# Edge-TTS Local Setup Guide

This repository allows you to generate AI voiceovers locally using **Edge-TTS** with Python.

---

## Prerequisites

Make sure the following are installed on your system:

- **Visual Studio Code (VS Code)**
- **Python** (added to system PATH)

> If Python is not added to PATH, follow a beginner YouTube tutorial for your OS.

---

## Installation & Setup

### 1. Download the Project
- Download the ZIP file from this repository  
- Extract it
- Open the extracted folder in **VS Code**

---

### 2. Install VS Code Extension
Install the following extension in VS Code:
- **Code Runner**

---

### 3. Project Structure

Inside the folder, you will see:

```
main.py
script.txt
```

- `main.py` → Python script to generate the voiceover  
- `script.txt` → Paste your text/script here  

---

### 4. Open Terminal in VS Code
Press:

```
Ctrl + `
```

This opens the integrated terminal.

---

### 5. Install Edge-TTS
Run the following command in the terminal:

```bash
pip install edge-tts
```

This installs Edge-TTS locally.

---

## How to Generate Voiceover

1. Paste your script into `script.txt`
2. Save the file (**Ctrl + S**)
3. Run `main.py`
4. Wait a few moments until the terminal confirms generation

A file named `voiceover.mp3` will be created.

You can move this file to any folder you want.

Every time you:
- Change `script.txt`
- Save it
- Run `main.py` again  

A new `voiceover.mp3` will be generated (previous one will be replaced).

---

## Changing the Voice

### Default Voice
```python
voice = "en-US-BrianMultilingualNeural"
```

---

### List Available Voices
Run this command in the terminal:

```bash
edge-tts --list-voices
```

---

### Change Voice
Copy a voice name from the list and replace it in `main.py`.

Example:
```python
voice = "en-GB-RyanNeural"
```

Save the file and run the script again.

---

## Notes
- Voice generation time depends on script length
- Always save `script.txt` before running
- Internet connection is required for Edge-TTS

---

## License
Free to use for personal and educational purposes.
