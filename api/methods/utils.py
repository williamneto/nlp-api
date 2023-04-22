import os
from transformers import pipeline

def get_generator(
    task: str = "text-generation",
    model: str = "egonrp/gpt2-medium-squadv11-portuguese"
):
    model_path = "./llms/"
    if not os.path.isdir("./llms"):
        os.mkdir(model_path)
        generator = pipeline(task, model=model)
    else:
        generator = pipeline(task, model=model_path)

    generator.save_pretrained(model_path)

    return generator

def clean_completion(completion: list):
    for item in completion:
        item["generated_text"] = item["generated_text"].split(
            "<|assistant|>"
        )[1]
    
    return completion