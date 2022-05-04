from abc import abstractmethod
from typing import List

from PIL.Image import Image

from config import Config
from figures.BoundingBox import BoundingBox
from figures.Circle import Circle
from figures.Triangle import Triangle
from randomizer.Randomizer import Randomizer


class Generator:

    def __init__(self):
        self.artifacts_b_boxes = []

    @abstractmethod
    def generate(self, img: Image) -> Image:
        pass

    def __export_artifacts(self, img: Image):
        pass
        # for b_box in self.artifacts_b_boxes:
        #     b_box.export(img)

    def __draw_artifacts_bounding_boxes(self, img: Image):
        for b_box in self.artifacts_b_boxes:
            img = b_box.draw(img)
        return img
