from transformers import pipeline, set_seed
from methods.utils import get_generator, clean_completion

def _complete(
    prompt: str,
    max_new_tokens: int = 120,
    num_return_sequences: int = 1,
    do_sample: bool = False
):
    generator = get_generator()
    result = generator(
        "<|prompter|>%s<|assistant|>" % prompt, 
        max_new_tokens=max_new_tokens, 
        num_return_sequences=num_return_sequences, 
        do_sample=do_sample
    )

    return clean_completion(
        result
    )