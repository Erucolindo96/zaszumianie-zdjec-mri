import tempfile
from typing import List
import nibabel as nib
from PIL import Image, ImageFilter
import numpy as np
import random
from figures.ArtifactsPositioner import ArtifactsPositioner
from figures.Generator import Generator


class TestImageCreator:
    def __init__(self, nifti_files_paths: List[str], generated_dir: str, generated_with_b_box_dir: str,
                 images_count: int):
        self.images = []
        self.generated_images_dir = generated_dir
        self.images_count = images_count
        self.generated_with_b_box_images_dir = generated_with_b_box_dir

        for nifti_path in nifti_files_paths:
            nifti = nib.load(nifti_path).get_data()
            for image_num in range(TestImageCreator.__image_cnt(nifti)):
                self.images.append(nifti[:, :, image_num].astype(np.uint8))

        self.artifact_positioner = ArtifactsPositioner(self.generated_images_dir)

    @staticmethod
    def __image_cnt(nifti) -> int:
        return nifti.shape[2]

    def create_with_artifacts(self):
        for art_img_num in range(self.images_count):
            plain_image_num = random.randint(0, len(self.images) - 1)
            plain_image = Image.fromarray(self.images[plain_image_num])
            plain_image = plain_image.convert('RGBA')

            generator = Generator()
            image = generator.generate(plain_image)

            (_, image_filepath) = tempfile.mkstemp(dir=self.generated_images_dir, suffix='.png')
            image_filename = image_filepath.split('/')[-1]
            image.save(image_filepath)

            self.__save_with_b_boxes(image, generator, image_filename)

            self.artifact_positioner.add_image(generator.artifacts_b_boxes, image_filename)

        self.artifact_positioner.generate_artifacts_pos_file()

    def __save_with_b_boxes(self, image: Image, generator: Generator, filename):
        for b_box in generator.artifacts_b_boxes:
            image = b_box.draw(image)
        image.save(f'{self.generated_with_b_box_images_dir}{filename}')

    def create(self):
        self.create_with_artifacts()
