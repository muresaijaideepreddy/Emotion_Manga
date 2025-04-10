# Emotion-Guided Manga Interpolation with Dynamic Crafter

This project demonstrates a novel application of the pretrained [Dynamic Crafter](https://huggingface.co/damo-vilab/dynamic-crafter) diffusion model for manga panel interpolation, guided by emotion transitions between the first and last panels.

## 🔍 Project Summary

We use emotion detection (via DeepFace) on the start and end panels to generate an emotionally meaningful prompt. This prompt guides the diffusion model to generate a realistic and expressive middle panel. The system also includes CLIP-based evaluation to measure similarity.

---

## 📁 Project Structure

```
emotion_manga/
├── app/                 # Core logic for model inference and emotion analysis
│   ├── __init__.py
│   ├── pipeline.py
│   ├── emotion.py
│   ├── prompt_utils.py
│   └── similarity.py
├── demo/                # Gradio interface for demo
│   ├── interface.py
│   └── launch.py
├── scripts/             # Scripts for batch generation and plotting
│   ├── batch_generate.py
│   └── emotion_chart.py
├── dataset/             # Contains triplets of manga panels (start, middle, end)
│   ├── scene1_start.png
│   ├── scene1_middle.png
│   └── scene1_end.png
├── output/              # Output folder for generated frames
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧪 Installation

```bash
git clone <your_repo_url>
cd emotion_manga

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Run the Interactive Demo

Launch the Gradio interface:

```bash
python demo/launch.py
```

Upload a **start** and **end** panel, and the system will:
1. Detect emotions using DeepFace.
2. Generate an emotion-guided prompt.
3. Use Dynamic Crafter to synthesize the middle frame.
4. Display the full transition!

---

## ⚙️ Run Batch Inference on Dataset

Make sure your images are in the `dataset/` folder as:
```
scene1_start.png, scene1_end.png
scene2_start.png, scene2_end.png
...
```

Run this script to generate middle panels:

```bash
python scripts/batch_generate.py
```

Results will be saved in the `output/` folder.

---

## 📈 Optional: Evaluate with CLIP or Plot Emotions

Use the CLIP-based similarity check (see `app/similarity.py`) or plot the emotional transition using:

```bash
from scripts.emotion_chart import plot_emotions
plot_emotions("happy", "neutral", "sad", "output/emotion_curve.png")
```

---

## 📦 Sample Dataset

A sample dataset with 5 dummy manga triplets is provided here:  
👉 [Download](sandbox:/mnt/data/emotion_manga_sample_dataset.zip)

---

## 🤖 Credits

- [Dynamic Crafter](https://huggingface.co/damo-vilab/dynamic-crafter) for pretrained interpolation
- [DeepFace](https://github.com/serengil/deepface) for emotion recognition
- [CLIP](https://huggingface.co/openai/clip-vit-base-patch32) for semantic similarity evaluation

---

## ✅ Project Achievements

- Emotion-guided prompt conditioning
- High-quality frame interpolation with pretrained models
- Interactive demo and batch generation
- Optional CLIP-based evaluation

