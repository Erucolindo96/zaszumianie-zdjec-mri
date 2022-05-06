from os import fdopen
from typing import List, Tuple

from PIL import ImageDraw
from PIL.Image import Image

from figures.Circle import Circle
from figures.Triangle import Triangle
import tempfile


class BoundingBox:
    def __init__(self, top_left: Tuple[int, int], bottom_right: Tuple[int, int], type: str):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.type = type

    @classmethod
    def from_point(cls, circle: Circle, radiuses: List[Triangle], bb_gain: int):
        circle_r = circle.radius
        max_radius = max(radiuses, key=lambda radius: radius.height) if radiuses else None

        bounding_box_side = max([max_radius.height, circle_r]) if max_radius else circle_r

        circle_pos = circle.pos
        top_left = tuple(coordinate - (bounding_box_side + bb_gain) for coordinate in circle_pos)
        bottom_right = tuple(coordinate + (bounding_box_side + bb_gain) for coordinate in circle_pos)
        return cls(top_left, bottom_right, 'point')

    @classmethod
    def from_elipse(cls, elipse_pos: Tuple[int, int], max_arm_len: int, bb_gain: int):
        top_left = tuple(coordinate - (max_arm_len + bb_gain) for coordinate in elipse_pos)
        bottom_right = tuple(coordinate + (max_arm_len + bb_gain) for coordinate in elipse_pos)
        return cls(top_left, bottom_right, 'elipse')

    @classmethod
    def from_stripes(cls, higher_point, lower_point, xy_last, bbox_gain):
        x_max = xy_last[0]
        y_last = xy_last[1]
        top_left_x = min(higher_point[0], lower_point[0]) - bbox_gain
        top_left_y = min(y_last, higher_point[1], lower_point[1]) - bbox_gain
        bottom_right_x = x_max + bbox_gain
        bottom_right_y = max(y_last, higher_point[1], lower_point[1]) + bbox_gain
        return cls((top_left_x, top_left_y), (bottom_right_x, bottom_right_y), 'stripe')

    def bounding_box_pos(self) -> List[Tuple[int, int]]:
        return [self.top_left, self.bottom_right]

    def as_point_and_size(self):
        pos = self.bounding_box_pos()
        x = pos[0][0]
        y = pos[0][1]
        w = pos[1][0] - pos[0][0]
        h = pos[1][1] - pos[0][1]
        return (x, y, w, h)

    def draw(self, img: Image) -> Image:
        draw = ImageDraw.Draw(img)
        draw.rectangle(self.bounding_box_pos(), outline='orange')
        return img

    def export(self, img: Image) -> Image:
        b_box = self.bounding_box_pos()
        artifact = img.crop(b_box[0] + b_box[1])
        artifact.save(self.artifact_file)
        return artifact
