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
                # b_boxes_poses = [b_box.bounding_box_pos() for b_box in img_artifacts]
                # b_boxes_writeable_poses = [b_box_pos[0] + b_box_pos[1] for b_box_pos in b_boxes_poses]
                b_boxes_writeable_poses = self.__cast_b_boxes_to_suitable_format(img_artifacts)
                line = f'{img_path} {art_num} {b_boxes_writeable_poses}\n'
                file.write(line)

    def __cast_b_boxes_to_suitable_format(self, b_boxes: List[BoundingBox]):
        b_boxes_as_string = ''
        b_box_sep = '   '

        for b_box in b_boxes:
            pos = b_box.bounding_box_pos()
            pos_as_string = str(pos[0][0]) + ' ' + str(pos[0][1]) + ' ' + str(pos[1][0]) + ' ' + str(
                pos[1][1]) + b_box_sep
            b_boxes_as_string += pos_as_string

        return b_boxes_as_string
