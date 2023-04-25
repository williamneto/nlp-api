from loguru import logger

from adapters.constants import DEFAULT_MODELS

from methods.utils import get_generator, clean_completion

def _classify(
    prompt: str,
    model: str = DEFAULT_MODELS["text-classification"]
):
    generator = get_generator(
        model=model,
        task="text-classification"
    )
    logger.debug(model)

    result = generator(
        prompt
    )

    return result