# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from nibabel.testing import data_path
from typing import Tuple, List

import PIL.Image
import nibabel as nib
import imageio
from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Press the green button in the gutter to run the script.
from PIL.ImageDraw import ImageDraw
from figures.Circle import Circle
from figures.Generator import Generator
from figures.Triangle import Triangle


def draw_circle(img: PIL.Image.Image, circle_pos: Tuple[int, int], radius: int) -> PIL.Image.Image:
    top_left = tuple(x - radius for x in circle_pos)
    bottom_right = tuple(x + radius for x in circle_pos)
    draw = PIL.ImageDraw.Draw(img)
    draw.ellipse(top_left + bottom_right, fill='white', outline='white')
    # draw.point((100, 100), 'red')
    return img


def draw_triangle(img: PIL.Image.Image, triangle: List[Tuple[int, int]]) -> PIL.Image.Image:
    draw = PIL.ImageDraw.Draw(img)
    draw.polygon(triangle, fill='white')
    return img


def draw_rectangle(img: PIL.Image.Image, top_left: Tuple[int, int], bottom_right: Tuple[int, int]) -> PIL.Image.Image:
    draw = PIL.ImageDraw.Draw(img)
    draw.rectangle([top_left, bottom_right], fill='white')
    return img


def gaussian_blur(img: PIL.Image.Image, top_left: Tuple[int, int], bottom_right: Tuple[int, int]) -> PIL.Image.Image:
    region = img.crop(top_left + bottom_right)
    filtered = region.filter(ImageFilter.GaussianBlur(radius=3))
    img.paste(filtered, top_left + bottom_right)
    return img


def main():
    generator = Generator()
    with Image.open('MRI_MSC_Dataset/sub-001/png/50.png') as image:
        image = generator.generate(image)
        image.save('MRI_MSC_Dataset/sub-001/png/50-szumy-auto-full.png')
        # circle = Circle((150, 150), radius=5)
        # triangle = Triangle(height=10, angle=2, center_circle=circle)
        # image = circle.draw(image)
        # image = triangle.draw(image)
        # image = triangle.blur(image)
        # image.save('MRI_MSC_Dataset/sub-001/png/50-szumy-auto.png')
        # circle = (150, 150)
        # radius = 5
        # triangle = [(150, 145), (150, 155), (170, 150)]
        #
        # top_left = (150, 148)
        # bottom_right = (170, 152)
        #
        # image = draw_circle(image, circle_pos=circle, radius=radius)
        # # image = draw_triangle(image, triangle=triangle)
        # image = draw_rectangle(image, top_left=top_left, bottom_right=bottom_right)
        # image = gaussian_blur(image, top_left=(150, 145), bottom_right=(170, 155))



if __name__ == '__main__':
    main()
    # nifti_file = '/home/krzysztof/PycharmProjects/zaszumianie-zdjec-mri/MRI_MSC_Dataset/sub-001/ses-1/anat/t2_spc2_an_Anonymized.nii.gz'
    # img = nib.load(nifti_file)
    # img_slice = img.get_data()[:, :, 115].astype(np.uint8)
    # img_affine = img.affine
    #
    # single_img = nib.Nifti1Image(img_slice, img_affine)
    # # imageio.imwrite('pic1.bmp', img_slice)
    # # im = Image.fromarray(img_slice)
    # # print(img_slice)
    # # img_slice = np.repeat(img_slice, repeats=3).reshape((256,256,3))
    # dupa = np.repeat(img_slice, repeats=3).reshape((256,256,3))
    # print(np.repeat(img_slice, repeats=3).reshape((256,256,3)))
    # # im.save("your_file.png")
    # matplotlib.pyplot.imsave('MRI_MSC_Dataset/sub-001/png/115.png', dupa)
    # print(img_slice.shape)
    # print(img.get_data_dtype())
    # print(max(dupa.reshape(256*256*3)))

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
