from app.pipeline import load_model, generate_middle_frame
from app.prompt_utils import get_emotion_prompt
from app.emotion import detect_emotion
from PIL import Image
import os

def process_pair(start_path, end_path, out_path):
    pipe = load_model()
    emotion_a = detect_emotion(start_path)
    emotion_c = detect_emotion(end_path)
    prompt = get_emotion_prompt(emotion_a, emotion_c)
    start = Image.open(start_path).convert("RGB")
    end = Image.open(end_path).convert("RGB")
    middle = generate_middle_frame(pipe, start, end, prompt)
    middle.save(out_path)

# Example usage:
# process_pair("inputs/scene1_start.png", "inputs/scene1_end.png", "output/scene1_middle.png")
