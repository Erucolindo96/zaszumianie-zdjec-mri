class Config:
    nifti_train_files = ['MRI_MSC_Dataset/sub-001/ses-1/anat/sub-001.nii.gz',
                          'MRI_MSC_Dataset/sub-002/ses-1/anat/sub-002.nii.gz',
                          'MRI_MSC_Dataset/sub-003/ses-1/anat/sub-003.nii.gz',
                          'MRI_MSC_Dataset/sub-004/ses-1/anat/sub-004.nii.gz',
                         ]

    train_generated_dir = '/home/krzysztof/Dokumenty/prywata/magisterka/datasets/sample/train/generated/'

    train_plain_files = '/home/krzysztof/Dokumenty/prywata/magisterka/datasets/sample/train/plain/'

    train_images_cnt = 10

    nifti_test_files = ['MRI_MSC_Dataset/sub-001/ses-1/anat/sub-001.nii.gz',
                        'MRI_MSC_Dataset/sub-002/ses-1/anat/sub-002.nii.gz',
                        'MRI_MSC_Dataset/sub-003/ses-1/anat/sub-003.nii.gz',
                        'MRI_MSC_Dataset/sub-004/ses-1/anat/sub-004.nii.gz',
                        ]
    test_generated_dir = '/home/krzysztof/Dokumenty/prywata/magisterka/datasets/sample/test/generated/'
    test_generated_with_b_box_dir = '/home/krzysztof/Dokumenty/prywata/magisterka/datasets/sample/test/bbox/'
    test_images_cnt = 10

    circle_min_r = 1
    circle_max_r = 4
    circle_pos_mean = 128
    circle_pos_sigma = 30
    triangle_min_angle = 0
    triangle_max_angle = 6.28
    triangle_min_h = 5
    triangle_max_h = 16

    alpha_max = 255
    alpha_min = 228

    min_triangle_cnt = 0
    max_triangle_cnt = 5

    min_circle_cnt = 1
    max_circle_cnt = 4

    bound_artifacts = False
    bounding_box_gain = 3
    export_artifacts = False
    export_artifacts_dir = 'MRI_MSC_Dataset/sub-001/artifacts/'
    blur_triangles = True
