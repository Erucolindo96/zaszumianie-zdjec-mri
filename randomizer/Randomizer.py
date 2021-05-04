import random
from random import Random
from typing import Tuple

from config import Config


class Randomizer:
    def __init__(self, random_seed: int = None):
        self.seed = random_seed
        self.random = Random()
        self.random.seed(random_seed) if random_seed is not None else self.random.seed()

    def circle_r(self) -> int:
        return self.random.randint(Config.circle_min_r, Config.circle_max_r)

    def circle_pos(self) -> Tuple[int, int]:
        return int(self.random.gauss(Config.circle_pos_mean, Config.circle_pos_sigma)), int(
            self.random.gauss(Config.circle_pos_mean, Config.circle_pos_sigma))

    def circle_cnt(self) -> int:
        return self.random.randint(Config.min_circle_cnt, Config.max_circle_cnt)

    def triangle_h(self) -> int:
        return self.random.randint(Config.triangle_min_h, Config.triangle_max_h)

    def triangle_angle(self) -> float:
        return self.random.uniform(Config.triangle_min_angle, Config.triangle_max_angle)

    def triangle_cnt(self) -> int:
        return self.random.randint(Config.min_triangle_cnt, Config.max_triangle_cnt)
