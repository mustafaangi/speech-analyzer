# Audio Transcription and Analysis App

This project is an audio transcription and analysis application built using Gradio and Hugging Face Transformers. It allows users to upload or record audio, transcribe the audio, and analyze the transcription.

## Features

- **Audio Transcription**: Transcribe audio files using the `openai/whisper-tiny.en` model.
- **Text Analysis**: Analyze transcriptions using the `TinyLlama/TinyLlama-1.1B-Chat-v1.0` model.
- **User Interface**: Simple and interactive UI built with Gradio.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mustafaangi/speech-analyzer.git
    cd speech-analyzer
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python speech_analyzer.py
    ```

2. Open the provided URL in your browser to access the application.

## Code Overview

### `speech_analyzer.py`
