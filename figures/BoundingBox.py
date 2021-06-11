from typing import List, Tuple

from PIL import ImageDraw
from PIL.Image import Image

from figures.Circle import Circle
from figures.Triangle import Triangle


class BoundingBox:
    def __init__(self, circle: Circle, radiuses: List[Triangle], bb_gain: int):
        self.circle = circle
        self.radiuses = radiuses
        self.bounding_box_gain = bb_gain

    def __bounding_box(self) -> List[Tuple[int, int]]:
        circle_r = self.circle.radius
        max_radius = max(self.radiuses, key=lambda radius: radius.height) if self.radiuses else None

        bounding_box_side = max([max_radius.height, circle_r]) if max_radius else circle_r

        circle_pos = self.circle.pos
        top_left = tuple(coordinate - (bounding_box_side + self.bounding_box_gain) for coordinate in circle_pos)
        bottom_right = tuple(coordinate + (bounding_box_side + self.bounding_box_gain) for coordinate in circle_pos)

        return [top_left, bottom_right]

    def draw(self, img: Image):
        draw = ImageDraw.Draw(img)
        draw.rectangle(self.__bounding_box(), outline='orange')
        return img
