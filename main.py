from TrainImageCreator import TrainImageCreator
from config import Config


def main():
    train_image_creator = TrainImageCreator(nifti_files_paths=Config.nifti_train_files,
                                            generated_dir=Config.train_generated_dir,
                                            plain_dir=Config.train_plain_files,
                                            iterations=Config.train_image_creating_iterations)

    train_image_creator.create()


if __name__ == '__main__':
    main()

    print('done')
