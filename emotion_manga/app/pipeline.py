from diffusers import DiffusionPipeline
import torch

def load_model():
    pipe = DiffusionPipeline.from_pretrained(
        "damo-vilab/dynamic-crafter", torch_dtype=torch.float16
    )
    return pipe.to("cuda")

def generate_middle_frame(pipe, start_img, end_img, prompt, steps=25):
    result = pipe(
        image=[start_img, end_img],
        prompt=prompt,
        num_inference_steps=steps,
        guidance_scale=7.5,
    )
    return result.images[0]
