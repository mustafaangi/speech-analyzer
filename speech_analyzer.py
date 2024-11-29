import gradio as gr
from transformers import pipeline
import torch
import warnings
import time
from functools import lru_cache

warnings.filterwarnings('ignore', category=FutureWarning)

class AnalysisConfig:
    def __init__(self):
        self.transcription_model = "openai/whisper-tiny.en"
        self.analysis_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        self.max_length = 512
        self.temperature = 0.7
        self.chat_prompt = """<|system|>You are a speech transcription assistant that accurately captures spoken words.
Your only task is to output exactly what was said in the audio, without analysis or additional commentary.

<|user|>Please transcribe this audio: {transcript}

<|assistant|>Here is what was said: {transcript}"""

@lru_cache(maxsize=1)
def load_models():
    """Cache models to avoid reloading."""
    config = AnalysisConfig()
    trans_pipe = pipeline(
        "automatic-speech-recognition",
        model=config.transcription_model,
        chunk_length_s=30,
    )
    analysis_pipe = pipeline(
        "text-generation",
        model=config.analysis_model,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    return trans_pipe, analysis_pipe

def transcript_audio(audio_file, progress=gr.Progress()):
    """Simply transcribe audio and return what was heard."""
    try:
        if not audio_file:
            return "Please provide an audio input."

        progress(0.3, desc="Loading transcription model...")
        trans_pipe = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-tiny.en",
            chunk_length_s=30,
        )
        
        progress(0.7, desc="Transcribing audio...")
        transcript_txt = trans_pipe(audio_file)["text"]
        
        return f"I heard: {transcript_txt}"

    except Exception as e:
        return f"Error transcribing audio: {str(e)}"

def check_audio_device():
    """Check if microphone is available"""
    try:
        import pyaudio
        audio = pyaudio.PyAudio()
        device_count = audio.get_device_count()
        audio.terminate()
        return device_count > 0
    except Exception as e:
        return False

with gr.Blocks(title="Audio Analysis App") as demo:
    gr.Markdown("# 🎙️ Audio Transcription and Analysis")
    gr.Markdown("""
    ### Instructions:
    - Record: Click on the microphone icon
    - Upload: Click to select an audio file
    - Supported: WAV, MP3, OGG
    """)

    with gr.Row():
        audio_input = gr.Audio(
            label="Upload or Record Audio",
            type="filepath",
            sources=["microphone", "upload"],
            format="wav"
        )

    with gr.Row():
        analyze_btn = gr.Button("Analyze", variant="primary")
        clear_btn = gr.Button("Clear", variant="secondary")

    output_text = gr.Textbox(
        label="Transcription",
        placeholder="Results will appear here...",
        lines=10,
    )

    def clear_inputs():
        return None, ""

    clear_btn.click(
        fn=clear_inputs,
        outputs=[audio_input, output_text],
    )

    analyze_btn.click(
        fn=transcript_audio,
        inputs=audio_input,
        outputs=output_text,
    )

if __name__ == "__main__":
    try:
        # Simple queue configuration without specific concurrency settings
        demo.queue().launch(
            server_name="0.0.0.0",
            share=True,
            show_error=True,
        )
    except Exception as e:
        print(f"Error starting server: {e}")
        # Optional: Print Gradio version for debugging
        import gradio as gr
        print(f"Gradio version: {gr.__version__}")