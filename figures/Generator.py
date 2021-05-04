from typing import List

from PIL.Image import Image

from figures.Circle import Circle
from figures.Triangle import Triangle
from randomizer.Randomizer import Randomizer


class Generator:

    def __init__(self):
        self.randomizer = Randomizer()

    def generate(self, img: Image) -> Image:
        circle_cnt = self.randomizer.circle_cnt()
        print('Circle cnt: {}'.format(circle_cnt))

        for i in range(circle_cnt):
            circle_pos = self.randomizer.circle_pos()
            circle_r = self.randomizer.circle_r()
            print("Circle pos:{}, r:{}".format(circle_pos, circle_r))

            electrode = Circle(pos=circle_pos, radius=circle_r)
            img = electrode.draw(img)
            noise_radiuses = self.__generate_noise_radiuses(drawed_electrode=electrode)
            for radius in noise_radiuses:
                img = radius.draw(img)
        return img

        # circle_pos = self.randomizer.circle_pos()
        # circle_r = self.randomizer.circle_r()
        # print("Circle pos:{}, r:{}".format(circle_pos, circle_r))
        #
        # electrode = Circle(pos=circle_pos, radius=circle_r)
        # img = electrode.draw(img)
        #
        # triangle_cnt = self.randomizer.triangle_cnt()
        # print("Triangle cnt: {}".format(triangle_cnt))
        # noise_radiuses = []
        #
        # for i in range(triangle_cnt):
        #     h = self.randomizer.triangle_h()
        #     angle = self.randomizer.triangle_angle()
        #     print('Triangle h: {}, angle in radians: {}'.format(h, angle))
        #
        #     radius = Triangle(height=h, angle=angle, center_circle=electrode)
        #     img = radius.draw(img)
        #     noise_radiuses.append(radius)

        # for radius in noise_radiuses:
        #     img = radius.blur(img)
        # return img

    def __generate_noise_radiuses(self, drawed_electrode: Circle) -> List[Triangle]:
        triangle_cnt = self.randomizer.triangle_cnt()
        print("Triangle cnt: {}".format(triangle_cnt))
        noise_radiuses = []

        for i in range(triangle_cnt):
            h = self.randomizer.triangle_h()
            angle = self.randomizer.triangle_angle()
            print('Triangle h: {}, angle in radians: {}'.format(h, angle))

            noise_radiuses.append(Triangle(height=h, angle=angle, center_circle=drawed_electrode))

        return noise_radiuses
