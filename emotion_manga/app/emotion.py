from deepface import DeepFace

def detect_emotion(img_path):
    result = DeepFace.analyze(img_path=img_path, actions=['emotion'], enforce_detection=False)
    return result[0]['dominant_emotion']
