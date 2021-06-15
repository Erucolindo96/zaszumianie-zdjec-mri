from typing import List

from figures.BoundingBox import BoundingBox


class ArtifactsPositioner:
    def __init__(self, generated_images_dest_dir: str):
        self.__artifacts = {}
        self.__dest_dir = generated_images_dest_dir
        self.__info_filename = '/info.dat'

    def add_image(self, artifacts_bounding_boxes: List[BoundingBox], image_filename: str):
        self.__artifacts[image_filename] = artifacts_bounding_boxes

    def generate_artifacts_pos_file(self):
        with open(self.__dest_dir + self.__info_filename, 'w') as file:
            for img_path, img_artifacts in self.__artifacts.items():
                art_num = len(img_artifacts)
                b_boxes_writeable_poses = self.__cast_b_boxes_to_suitable_format(img_artifacts)
                line = f'{img_path} {art_num} {b_boxes_writeable_poses}\n'
                file.write(line)

    def __cast_b_boxes_to_suitable_format(self, b_boxes: List[BoundingBox]):
        b_boxes_as_string = ''
        b_box_sep = '   '

        for b_box in b_boxes:
            (x, y, w, h) = b_box.as_point_and_size()
            pos_as_string = str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + b_box_sep
            b_boxes_as_string += pos_as_string

        return b_boxes_as_string
