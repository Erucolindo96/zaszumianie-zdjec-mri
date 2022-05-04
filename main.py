from creators.TestImageCreator import TestImageCreator
from creators.TrainImageCreator import TrainImageCreator
from config import Config
from figures.PointArtifactGenerator import PointArtifactGenerator
from figures.StarArtifactGenerator import StarArtifactGenerator


def main():
    generator = None
    if Config.artifact_type == 'point':
        generator = PointArtifactGenerator()
    if Config.artifact_type == 'stars':
        generator = StarArtifactGenerator()

    print('generate training images')
    train_image_creator = TrainImageCreator(nifti_files_paths=Config.nifti_train_files,
                                            generated_dir=Config.train_generated_dir,
                                            plain_dir=Config.train_plain_files,
                                            images_count=Config.train_images_cnt, generator=generator)

    train_image_creator.create()
    print('train images generation was done')

    print('generate test images')
    test_image_creator = TestImageCreator(nifti_files_paths=Config.nifti_test_files,
                                          generated_with_b_box_dir=Config.test_generated_with_b_box_dir,
                                          generated_dir=Config.test_generated_dir, images_count=Config.test_images_cnt,
                                          generator=generator)
    test_image_creator.create()
    print('test images generation was done')


if __name__ == '__main__':
    main()

    print('done')
