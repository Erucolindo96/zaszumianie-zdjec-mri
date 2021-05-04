from typing import Tuple

from PIL.Image import Image
from PIL import ImageDraw
from PIL import ImageFilter


class Circle:

    def __init__(self, pos: Tuple[int, int], radius: int):
        self.pos = pos
        self.radius = radius

    def __top_left(self):
        return tuple(x - self.radius for x in self.pos)

    def __bottom_right(self):
        return tuple(x + self.radius for x in self.pos)

    def draw(self, img: Image) -> Image:
        top_left = self.__top_left()
        bottom_right = self.__bottom_right()
        draw = ImageDraw.Draw(img)
        draw.ellipse(top_left + bottom_right, fill='white', outline='white')
        return img

    def blur(self, img: Image) -> Image:
        top_left = self.__top_left()
        bottom_right = self.__bottom_right()

        region = img.crop(top_left + bottom_right)
        filtered = region.filter(ImageFilter.GaussianBlur(radius=1))
        img.paste(filtered, top_left + bottom_right)
        return img
