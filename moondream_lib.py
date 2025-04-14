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
    
    #using previous detect method will result in error : sequence item 0: expected str instance, dict found
    # So i have modified the detect method to return a string representation of the detected objects.
    # This is a simple example; you may want to format the output differently based on your needs.
    def detect(self, image: Union[Image.Image, str], object: str) -> str:
        img = self._load_image(image)
        detect = self.model.query(img, object)
        # Assuming `detect` is a dictionary, format it as a string
        if isinstance(detect, dict):
         return ", ".join(f"{key}: {value}" for key, value in detect.items())
        elif isinstance(detect, list):
            return ", ".join(str(item) for item in detect)
        else:
            return str(detect)
    
    def _load_image(self, image: Union[Image.Image, str]) -> Image.Image:
        if isinstance(image, str):
            return Image.open(image)
        return image