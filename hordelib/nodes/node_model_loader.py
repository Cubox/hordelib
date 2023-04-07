# node_model_loader.py
# Simple proof of concept custom node to load models.

from loguru import logger


class HordeCheckpointLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_manager": ("<model manager instance>",),
                "model_name": ("<model name>",),
            },
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "load_checkpoint"

    CATEGORY = "loaders"

    def load_checkpoint(
        self,
        model_manager,
        model_name,
        output_vae=True,
        output_clip=True,
    ):

        logger.debug(f"Loading model {model_name} through our custom node")

        if model_manager.manager is None:
            logger.error("horde_model_manager appears to be missing!")
            raise RuntimeError  # XXX better guarantees need to be made

        if model_name not in model_manager.manager.loaded_models:
            logger.error(f"Model {model_name} is not loaded")
            raise RuntimeError  # XXX better guarantees need to be made

        return model_manager.manager.loaded_models[model_name]


NODE_CLASS_MAPPINGS = {"HordeCheckpointLoader": HordeCheckpointLoader}
