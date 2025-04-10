from transformers import CLIPModel, CLIPProcessor
import torch

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to("cuda")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def clip_similarity(img1, img2):
    inputs = clip_processor(images=[img1, img2], return_tensors="pt").to("cuda")
    features = clip_model.get_image_features(**inputs)
    return torch.nn.functional.cosine_similarity(features[0], features[1], dim=0).item()
