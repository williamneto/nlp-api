from transformers import pipeline, set_seed
from loguru import logger

from adapters.constants import DEFAULT_MODELS

from methods.utils import get_generator, clean_completion

def _complete(
    prompt: str,
    max_new_tokens: int = 120,
    num_return_sequences: int = 1,
    do_sample: bool = False,
    model: str = DEFAULT_MODELS["text-generation"]
):
    generator = get_generator(model=model)
    logger.debug(model)
    result = generator(
        "<|prompter|>%s<|assistant|>" % prompt, 
        max_new_tokens=max_new_tokens, 
        num_return_sequences=num_return_sequences, 
        do_sample=do_sample
    )

    return clean_completion(
        result
    )