import tempfile
from typing import List
import nibabel as nib
from PIL import Image, ImageFilter
import numpy as np

from figures.ArtifactsPositioner import ArtifactsPositioner
from figures.Generator import Generator


class TrainImageCreator:
    def __init__(self, nifti_files_paths: List[str], generated_dir: str, plain_dir: str, iterations: int):
        self.nifti_files = {}
        self.generated_images_dir = generated_dir
        self.plain_images_dir = plain_dir
        self.iterations = iterations

        for nifti_path in nifti_files_paths:
            nifti_filename_without_extention = nifti_path.split('/')[-1].split('.')[0]
            self.nifti_files[nifti_filename_without_extention] = nib.load(nifti_path).get_data()

        self.artifact_positioner = ArtifactsPositioner(self.generated_images_dir)

    @staticmethod
    def __image_cnt(nifti) -> int:
        return nifti.shape[2]

    def create(self):
        for iter in range(self.iterations):
            for (filename, nifti) in self.nifti_files.items():
                for image_num in range(TrainImageCreator.__image_cnt(nifti)):
                    curr_image = nifti[:, :, image_num].astype(np.uint8)
                    image = Image.fromarray(curr_image)

                    generator = Generator()
                    image = generator.generate(image)

                    (_, image_filepath) = tempfile.mkstemp(dir=self.generated_images_dir, suffix='.png')
                    image_filename = image_filepath.split('/')[-1]
                    image.save(image_filepath)

                    self.artifact_positioner.add_image(generator.artifacts_b_boxes, image_filename)

                    orig_image = Image.fromarray(curr_image)
                    orig_image.save(self.plain_images_dir + image_filename)

        self.artifact_positioner.generate_artifacts_pos_file()
