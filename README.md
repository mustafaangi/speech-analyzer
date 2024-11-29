```markdown
# Speech Analyzer

This is a speech transcription application that uses Gradio for the user interface and Hugging Face's Transformers library for speech-to-text and text analysis.

## Features

- Transcribe audio using the `openai/whisper-tiny.en` model.
- Analyze transcriptions using the `TinyLlama/TinyLlama-1.1B-Chat-v1.0` model.
- Simple and intuitive user interface built with Gradio.

## Requirements

- Python 3.11
- Homebrew (for macOS users)

## Installation

### 1. Install Homebrew (macOS only)

If you don't have Homebrew installed, you can install it using the following command:
```
```bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

### 2. Install Python 3.11

```bash
brew install python@3.11
```

### 3. Set up the virtual environment

Navigate to your project directory and create a virtual environment:

```bash
cd /path/to/speech-analyzer
python3.11 -m venv venv
source venv/bin/activate
```

### 4. Upgrade pip and install build tools

```bash
pip install --upgrade pip setuptools wheel
```

### 5. Install system dependencies

```bash
brew install pkg-config
brew install protobuf
brew install sentencepiece
```
Set the `PKG_CONFIG_PATH` environment variable:

```bash
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig:$PKG_CONFIG_PATH"
```

### 6. Install Python packages

Create a `requirements.txt` file with the following content:

```text
torch>=2.1.0
torchvision>=0.16.0
torchaudio>=2.1.0
transformers==4.35.2
gradio==3.50.2
pyaudio==0.2.13
sentencepiece
protobuf
```
Install the packages:

```bash
pip install -r 

requirements.txt


### 7. Verify package installation

Confirm that `torch` and other packages are installed correctly:

```bash
python -c "import torch; print(torch.__version__)"
```
## Running the Application

To run the application, use the following command:

```bash
python3

speech_analyzer.py

```

## Usage

1. Open the Gradio interface in your web browser.
2. Upload an audio file or record audio directly.
3. Click the "Transcribe" button to get the transcription.
4. The transcription will be displayed in the interface.

## Troubleshooting

If you encounter any issues, please ensure that all dependencies are installed correctly and that you are using Python 3.11. If problems persist, feel free to open an issue or contact the maintainer.


### **Summary**

This 

README.md

 file provides a comprehensive guide for setting up and running your speech analyzer application. It includes instructions for installing dependencies, setting up the virtual environment, and running the application. If you have any specific requirements or additional features, you can modify the README accordingly.
