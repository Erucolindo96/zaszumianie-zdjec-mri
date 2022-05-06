import tempfile
from typing import List
import nibabel as nib
from PIL import Image, ImageFilter
import numpy as np
import os.path
import random
from figures.ArtifactsPositioner import ArtifactsPositioner
from figures.Generator import Generator


class TrainImageCreator:
    def __init__(self, nifti_files_paths: List[str], generated_dir: str, plain_dir: str, images_count: int,
                 generator: Generator):
        self.images = []
        self.generated_images_dir = generated_dir
        self.plain_images_dir = plain_dir
        self.images_count = images_count
        self.generator = generator

        for nifti_path in nifti_files_paths:
            nifti = nib.load(nifti_path).get_data()
            for image_num in range(self.__image_cnt(nifti)):
                self.images.append(nifti[:, :, image_num].astype(np.uint8))

        self.artifact_positioner = ArtifactsPositioner(self.generated_images_dir)

    def __image_cnt(self, nifti) -> int:
        return nifti.shape[2]

    def create_with_artifacts(self):
        for image_num in range(self.images_count):
            plain_image_num = random.randint(0, len(self.images) - 1)
            plain_image = Image.fromarray(self.images[plain_image_num])
            plain_image = plain_image.convert('RGBA')

            image = self.generator.generate(plain_image)

            (_, image_filepath) = tempfile.mkstemp(dir=self.generated_images_dir, suffix='.png')
            image_filename = image_filepath.split('/')[-1]
            image.save(image_filepath)

            self.artifact_positioner.add_image(self.generator.artifacts_b_boxes, image_filename)
            self.generator.clean()

        self.artifact_positioner.generate_artifacts_pos_file()

    def create_plain_images(self):
        for image_num in range(len(self.images)):
            path = os.path.join(self.plain_images_dir, f'{image_num}.png')
            Image.fromarray(self.images[image_num]).save(path)

    def create(self):
        self.create_with_artifacts()
        self.create_plain_images()
