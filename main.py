import nibabel as nib
from PIL import Image, ImageFilter
import numpy as np

from TrainImageCreator import TrainImageCreator
from config import Config
from figures.ArtifactsPositioner import ArtifactsPositioner
from figures.Generator import Generator


def main():
    # nifti_file_path = Config.nifti_file
    # dest_dir = Config.dest_dir
    # orig_img_dir = Config.orig_files

    train_image_creator = TrainImageCreator(nifti_files_paths=Config.nifti_train_files, generated_dir=Config.train_generated_dir,
                                            plain_dir=Config.train_plain_files, iterations=Config.train_image_creating_iterations)

    train_image_creator.create()




#
# def generate_image(img_num: int, nifti_file: np.array, dest_dir: str):
#     image = Image.fromarray(nifti_file[:, :, img_num].astype(np.uint8))
#     generator = Generator()
#     image = generator.generate(image)
#     image.save(dest_dir + '{}.png'.format(img_num))


if __name__ == '__main__':
    main()

    print('dupa)')

    # wnioski
    # 1. mozna uzyc imageio, ono castuje to do uint8 bo max wartosc bitu to 222
    # 2. matplotlib, pomimo skomplikowania, wydaje sie bardziej perspektywiczny, bo w nim bde rysował
    # 3. matplotlib robi te zdjecia troche za ciemne - upewnij sie, ze nie skaluje ich wartości tak, by max to było białe
    # (może własnie on nie skaluje, za to ImageJ skaluje, i dlatego tam jest jasniej)
    # 4. W kolejnym kroku:
    #     a) Narysuj kilku - pikselowy okrąg w środku obrazu, ale by był widoczny, jako maksymalny biały (255)
    #     b) zachowac obecne skrypty, zeby nie zgubić sposobu zapisu obrazu do png
    #     c) Spróbój zrobić rozmycie gaussa na obwodzie koła - może to wystarczy by zasymulowac ten artefakt

    # Białe koło i trójkąty wyglądają obiecująco, tylko trzeba im dorobić rozmycie gaussa
    # Ogarnij, jak wydzielic z obrazu interesujący wycinek, zrobić na nim rozmycie gaussa i wrzucic znowu do numpy array
    # https: // pillow.readthedocs.io / en / 3.0.x / handbook / tutorial.html  # cutting-pasting-and-merging-images

# plan:
# 1. fcje które będa automatycznie obliczac koordynaty obiektów na podstawie parametrów(srodek koła, promień koła, wysokość trójkąta)
# żeby mozna było zeby mozna bylo wyliczac gdzie zrobic rozmycie gaussowskie
# 2. złożyc do kupy, zobaczyc czy działą
# 3. Zrobić fcje do losowania parsametrów(środek koła, promień koła, ilośc trójkątów, wysokości trójkątów)
# powinien to byc jakis rozkłąd gaussa dla promienia wysokości i ilości, równomierny dla środka koła(ale zeby mozna było zmienic w razie czego)
# 4. Zobacyzć jak działa
