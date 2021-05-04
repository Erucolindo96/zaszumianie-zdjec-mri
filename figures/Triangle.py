from math import sin, cos

from PIL.Image import Image
from PIL import ImageDraw, ImageFilter

from figures.Circle import Circle


class Triangle:
    def __init__(self, height: int, angle: float, center_circle: Circle):
        self.height = height
        self.angle = angle
        self.center_circle = center_circle

    def __first_base_point(self):
        (c_x, c_y) = self.center_circle.pos
        r = self.center_circle.radius
        return int(c_x + r * sin(self.angle)), int(c_y - r * cos(self.angle))

    def __second_base_point(self):
        (c_x, c_y) = self.center_circle.pos
        r = self.center_circle.radius
        return int(c_x - r * sin(self.angle)), int(c_y + r * cos(self.angle))

    def __height_point(self):
        (c_x, c_y) = self.center_circle.pos
        r = self.center_circle.radius
        return int(c_x + self.height * cos(self.angle)), int(c_y + self.height * sin(self.angle))

    def __triangle(self):
        return self.__first_base_point(), self.__second_base_point(), self.__height_point()

    def __top_left(self):
        triangle = self.__triangle()
        min_x = min(triangle, key=lambda point: point[0])[0]
        min_y = min(triangle, key=lambda point: point[1])[1]
        return min_x - 1, min_y - 1

    def __bottom_right(self):
        triangle = self.__triangle()
        max_x = max(triangle, key=lambda point: point[0])[0]
        max_y = max(triangle, key=lambda point: point[1])[1]
        return max_x + 1, max_y + 1

    def draw(self, img: Image) -> Image:
        draw = ImageDraw.Draw(img)
        triangle = self.__triangle()
        draw.polygon(triangle, fill='white')
        return img

    def blur(self, img: Image) -> Image:
        top_left = self.__top_left()
        bottom_right = self.__bottom_right()

        region = img.crop(top_left + bottom_right)
        filtered = region.filter(ImageFilter.GaussianBlur(radius=1))
        img.paste(filtered, top_left + bottom_right)
        return img
