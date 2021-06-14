from creators.TestImageCreator import TestImageCreator
from creators.TrainImageCreator import TrainImageCreator
from config import Config


def main():
    # train_image_creator = TrainImageCreator(nifti_files_paths=Config.nifti_train_files,
    #                                         generated_dir=Config.train_generated_dir,
    #                                         plain_dir=Config.train_plain_files,
    #                                         iterations=Config.train_image_creating_iterations)
    #
    # train_image_creator.create()
    test_image_creator = TestImageCreator(nifti_files_paths=Config.nifti_test_files,
                                          generated_with_b_box_dir=Config.test_generated_with_b_box_dir,
                                          generated_dir=Config.test_generated_dir, images_count=Config.test_images_cnt)
    test_image_creator.create()


if __name__ == '__main__':
    main()

    print('done')
