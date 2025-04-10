def get_emotion_prompt(start_emotion, end_emotion):
    transitions = {
        ("neutral", "angry"): "The character looks tense and alert.",
        ("happy", "sad"): "The character’s face falls into confusion.",
        ("sad", "angry"): "The sadness transforms into frustrated anger.",
    }
    return transitions.get((start_emotion, end_emotion), "The character changes emotionally.")
