import os
from transformers import pipeline
from loguru import logger

def get_generator(
    model: str,
    task: str = "text-generation"
):
    model_dir = "./llms/"
    model_name = model.split("/")[1]
    logger.debug(model_name)
    if not os.path.isdir("./llms"):
        os.mkdir(model_dir)
    
    if not os.path.isdir("%s%s" % (model_dir, model_name)):
        os.mkdir("%s%s" % (model_dir, model_name))
        generator = pipeline(task, model=model)
    else:
        try:
            generator = pipeline(task, model="%s%s" % (model_dir, model_name))
        except Exception as e:
            logger.debug(e)
            generator = pipeline(task, model=model)

    generator.save_pretrained("%s%s" % (model_dir, model_name))

    return generator

def clean_completion(completion: list):
    logger.debug(completion)
    for item in completion:
        item["generated_text"] = item["generated_text"].split(
            "<|assistant|>"
        )[1]
    
    return completion