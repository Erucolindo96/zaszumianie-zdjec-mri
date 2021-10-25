from typing import List

from PIL.Image import Image

from config import Config
from figures.BoundingBox import BoundingBox
from figures.Circle import Circle
from figures.Triangle import Triangle
from randomizer.Randomizer import Randomizer


class Generator:

    def __init__(self):
        self.randomizer = Randomizer()
        self.artifacts_b_boxes = []

    def generate(self, img: Image) -> Image:
        circle_cnt = self.randomizer.circle_cnt()
        print('Circle cnt: {}'.format(circle_cnt))
        for i in range(circle_cnt):
            circle_pos = self.randomizer.circle_pos()
            circle_r = self.randomizer.circle_r()
            alpha_channel = self.randomizer.transparency()
            print("Circle pos:{}, r:{}".format(circle_pos, circle_r))
            print('transparency: {}'.format(alpha_channel))

            electrode = Circle(pos=circle_pos, radius=circle_r, alpha=alpha_channel)
            img = electrode.draw(img)
            # img = electrode.blur(img)
            noise_radiuses = self.__generate_noise_radiuses(drawed_electrode=electrode, alpha=alpha_channel)
            for radius in noise_radiuses:
                img = radius.draw(img)
                if Config.blur_triangles:
                    img = radius.blur(img)

            if not noise_radiuses:
                img = electrode.blur(img)

            self.artifacts_b_boxes.append(
                BoundingBox(electrode, noise_radiuses, Config.bounding_box_gain, Config.export_artifacts_dir))

        if Config.export_artifacts:
            self.__export_artifacts(img)
        if Config.bound_artifacts:
            img = self.__draw_artifacts_bounding_boxes(img)
        return img

    def __export_artifacts(self, img: Image):
        pass
        # for b_box in self.artifacts_b_boxes:
        #     b_box.export(img)

    def __draw_artifacts_bounding_boxes(self, img: Image):
        for b_box in self.artifacts_b_boxes:
            img = b_box.draw(img)
        return img

    def __generate_noise_radiuses(self, drawed_electrode: Circle, alpha: int) -> List[Triangle]:
        triangle_cnt = self.randomizer.triangle_cnt()
        print("Triangle cnt: {}".format(triangle_cnt))
        noise_radiuses = []

        for i in range(triangle_cnt):
            h = self.randomizer.triangle_h()
            angle = self.randomizer.triangle_angle()
            print('Triangle h: {}, angle in radians: {}'.format(h, angle))

            noise_radiuses.append(Triangle(height=h, angle=angle, center_circle=drawed_electrode, alpha=alpha))

        return noise_radiuses
