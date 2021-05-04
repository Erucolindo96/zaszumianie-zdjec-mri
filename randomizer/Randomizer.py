import random
from random import Random
from typing import Tuple


class Randomizer:
    def __init__(self, random_seed: int = None):
        self.min_r = 1
        self.max_r = 10
        self.pos_mean = 128
        self.pos_sigma = 30
        self.min_angle = 0
        self.max_angle = 6.28
        self.min_h = 5
        self.max_h = 20

        self.min_triangle_cnt = 0
        self.max_triangle_cnt = 5

        self.min_circle = 1
        self.max_circle = 4

        self.seed = random_seed
        self.random = Random()
        self.random.seed(random_seed) if random_seed is not None else self.random.seed()

    def circle_r(self) -> int:
        return self.random.randint(self.min_r, self.max_r)

    def circle_pos(self) -> Tuple[int, int]:
        return int(self.random.gauss(self.pos_mean, self.pos_sigma)), int(
            self.random.gauss(self.pos_mean, self.pos_sigma))

    def circle_cnt(self) -> int:
        return self.random.randint(self.min_circle, self.max_circle)

    def triangle_h(self) -> int:
        return self.random.randint(self.min_h, self.max_h)

    def triangle_angle(self) -> float:
        return self.random.uniform(self.min_angle, self.max_angle)

    def triangle_cnt(self) -> int:
        return self.random.randint(self.min_triangle_cnt, self.max_triangle_cnt)
