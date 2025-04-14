from typing import Union
import moondream as md
from PIL import Image


class MoondreamHelper:
    # Init moondream model
    def __init__(self, api_key=None):
        self.model = md.vl(api_key=api_key)

    # Generate a description
    def describe(self, image: Union[Image.Image, str], detail: str = "normal") -> str:
        img = self._load_image(image)
        caption = self.model.caption(img, length=detail)
        return caption["caption"]
    
    # Query the image
    def query(self, image: Union[Image.Image, str], question: str) -> str:
        img = self._load_image(image)
        query = self.model.query(img, question)
        return query["answer"]
    
    # Detect objects in the image
    def detect(self, image: Union[Image.Image, str], question: str) -> str:
        img = self._load_image(image)
        detection = self.model.query(img, question)
        return detection["answer"]
    
    # Visual Pointing
    def visual_pointing(self, image: Union[Image.Image, str], question: str) -> str:
        img = self._load_image(image)
        pointing = self.model.query(img, question)
        return pointing["answer"]
    
    def _load_image(self, image: Union[Image.Image, str]) -> Image.Image:
        if isinstance(image, str):
            return Image.open(image)
        return image
    
    