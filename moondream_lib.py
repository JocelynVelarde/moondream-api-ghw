from typing import Union
import moondream as md  
from PIL import Image

class MoondreamHelper:
    def __init__(self, api_key=None):
        self.model = md.vl(api_key=api_key)

    def describe(self, image: Union[Image.Image, str], detail: str = "normal") -> str:
        img = self._load_image(image)
        response = self.model.caption(img, length=detail)
        return response.get("caption", "No caption returned.")

    def query(self, image: Union[Image.Image, str], question: str) -> str:
        img = self._load_image(image)
        response = self.model.query(img, question)
        return response.get("answer", "No answer returned.")

    def detect(self, image: Union[Image.Image, str], question: str) -> str:
        img = self._load_image(image)
        response = self.model.query(img, question)
        return response.get("answer", "No detection info returned.")

    def point(self, image: Union[Image.Image, str], target: str) -> str:
        img = self._load_image(image)
        response = self.model.point(img, target)
        return response.get("answer", "No visual pointing result returned.")

    def _load_image(self, image: Union[Image.Image, str]) -> Image.Image:
        if isinstance(image, str):
            return Image.open(image)
        return image
