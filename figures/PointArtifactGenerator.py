from typing import List

from PIL.Image import Image

from config import Config
from figures.BoundingBox import BoundingBox
from figures.Circle import Circle
from figures.Triangle import Triangle
from randomizer.Randomizer import Randomizer
from figures.Generator import Generator


class PointArtifactGenerator(Generator):

    def __init__(self):
        super().__init__()
        self.randomizer = Randomizer()

    def generate(self, img: Image) -> Image:
        img = img.convert('RGBA')
        circle_cnt = self.randomizer.circle_cnt()
        for i in range(circle_cnt):
            circle_pos = self.randomizer.circle_pos()
            circle_r = self.randomizer.circle_r()
            alpha_channel = self.randomizer.transparency()

            electrode = Circle(pos=circle_pos, radius=circle_r, alpha=alpha_channel)
            img = electrode.draw(img)
            noise_radiuses = self.__generate_noise_radiuses(drawed_electrode=electrode, alpha=alpha_channel)
            for radius in noise_radiuses:
                img = radius.draw(img)
                if Config.blur_triangles:
                    img = radius.blur(img)

            if not noise_radiuses:
                img = electrode.blur(img)

            self.artifacts_b_boxes.append(BoundingBox.from_point(electrode, noise_radiuses, Config.bounding_box_gain))

        if Config.export_artifacts:
            self.__export_artifacts(img)
        if Config.bound_artifacts:
            img = self.__draw_artifacts_bounding_boxes(img)
        return img

    def __generate_noise_radiuses(self, drawed_electrode: Circle, alpha: int) -> List[Triangle]:
        triangle_cnt = self.randomizer.triangle_cnt()
        noise_radiuses = []

        for i in range(triangle_cnt):
            h = self.randomizer.triangle_h()
            angle = self.randomizer.triangle_angle()

            noise_radiuses.append(Triangle(height=h, angle=angle, center_circle=drawed_electrode, alpha=alpha))

        return noise_radiuses
