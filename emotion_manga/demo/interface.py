import gradio as gr
from app.pipeline import load_model, generate_middle_frame
from app.emotion import detect_emotion
from app.prompt_utils import get_emotion_prompt
from PIL import Image

pipe = load_model()

def run_pipeline(start, end):
    start_path = "temp_start.png"
    end_path = "temp_end.png"
    start.save(start_path)
    end.save(end_path)

    emotion1 = detect_emotion(start_path)
    emotion2 = detect_emotion(end_path)
    prompt = get_emotion_prompt(emotion1, emotion2)

    middle = generate_middle_frame(pipe, start, end, prompt)
    return emotion1, emotion2, prompt, middle

iface = gr.Interface(
    fn=run_pipeline,
    inputs=[gr.Image(label="Start Frame"), gr.Image(label="End Frame")],
    outputs=[
        gr.Text(label="Emotion A"),
        gr.Text(label="Emotion C"),
        gr.Text(label="Interpolated Prompt"),
        gr.Image(label="Generated Middle Frame"),
    ],
    title="Emotion-Guided Manga Interpolation"
)
