from abc import abstractmethod

from PIL.Image import Image


class Generator:

    def __init__(self):
        self.artifacts_b_boxes = []
        self.randomizer = None

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

    def clean(self):
        self.artifacts_b_boxes = []
