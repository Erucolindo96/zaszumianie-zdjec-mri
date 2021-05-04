class Config:
    nifti_file = '/home/krzysztof/PycharmProjects/zaszumianie-zdjec-mri/MRI_MSC_Dataset/sub-001/ses-1/anat/t2_spc2_an_Anonymized.nii.gz'
    dest_dir = 'MRI_MSC_Dataset/sub-001/png/'

    circle_min_r = 1
    circle_max_r = 10
    circle_pos_mean = 128
    circle_pos_sigma = 30
    triangle_min_angle = 0
    triangle_max_angle = 6.28
    triangle_min_h = 5
    triangle_max_h = 20

    min_triangle_cnt = 0
    max_triangle_cnt = 5

    min_circle_cnt = 1
    max_circle_cnt = 4