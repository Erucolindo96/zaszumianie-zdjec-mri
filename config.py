class Config:
    nifti_train_files = [
        # 'MRI_MSC_Dataset/sub-001/ses-1/anat/sub-001.nii.gz',
        # 'MRI_MSC_Dataset/sub-002/ses-1/anat/sub-002.nii.gz',
        'MRI_MSC_Dataset/sub-003/ses-1/anat/sub-003.nii.gz',
        # 'MRI_MSC_Dataset/sub-004/ses-1/anat/sub-004.nii.gz',
    ]

    train_generated_dir = '/home/krzysztof/Dokumenty/prywata/magisterka/datasets/p_m_3_4/train/generated/'

    train_plain_files = '/home/krzysztof/Dokumenty/prywata/magisterka/datasets/p_m_3_4/train/plain/'

    train_images_cnt = 1000

    nifti_test_files = [
        # 'MRI_MSC_Dataset/sub-001/ses-1/anat/sub-001.nii.gz',
        # 'MRI_MSC_Dataset/sub-002/ses-1/anat/sub-002.nii.gz',
        # 'MRI_MSC_Dataset/sub-003/ses-1/anat/sub-003.nii.gz',
        'MRI_MSC_Dataset/sub-004/ses-1/anat/sub-004.nii.gz',
    ]
    test_generated_dir = '/home/krzysztof/Dokumenty/prywata/magisterka/datasets/p_m_3_4/test/generated/'
    test_generated_with_b_box_dir = '/home/krzysztof/Dokumenty/prywata/magisterka/datasets/p_m_3_4/test/bbox/'
    test_images_cnt = 1000

    circle_min_r = 1
    circle_max_r = 2  # for big points-> 4 for small -> 2 for small in 3/4 nifti -> 2
    circle_pos_mean = 200  # for 3/4 niftis-> 200 # for 1/2 niftis -> 128
    circle_pos_sigma = 60  # for 3/4 niftis -> 60 # for 1/2 niftis -> 30
    triangle_min_angle = 0
    triangle_max_angle = 6.28
    triangle_min_h = 2  # for big points->5 for small -> 2 for small in 3/4 nifti -> 2
    triangle_max_h = 7  # for big points->16 for small -> 5 for small in 3/4/ nifti -> 7

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

    artifact_type = 'point'  # available ['point', 'stars']

    stars = {
        'ARTIFACTS_ELIPSE': {
            "RANDOM_SEED": 32,
            "RADIUS_MIN": (1.5, 1.9),  # for 1/2 niftis -> (1.5, 1.9),
            "RADIUS_MAX": (8.0, 9.0),  # for 1/2 niftis -> (4.5, 5.1),
            "CIRCLE_POS_X_RANGE": [100, 300],  # for 1/2 niftis ->[100.0, 150.0],
            "CIRCLE_POS_Y_RANGE": [110.0, 310.0],  # for 1/2 niftis ->[110.0, 160.0],
            "TRANSPARENCY": 255,
            "GRADIENT_RANGE": [115, 255],
            "LEVELS": 15,
            'COUNT_MIN': 1,
            'COUNT_MAX': 2,
            'MIN_DIST': 60
        },
        'ARTIFACTS_NORD_ARM': {
            "HIGH_MIN": [3.5, 5],  # for 1/2 niftis -> [3.5, 5],
            "HIGH_MAX": [10, 12],  # for 1/2 niftis -> [10, 12],
            "ALPHA": [80, 75],
            "BETA": [105, 100],
            "GRADIENT_RANGE": [115, 255],
            "TRANSPARENCY": 255,
            "LEVELS": 15
        },
        'ARTIFACTS_NORD_EAST_ARM': {
            "HIGH_MIN": [3.4, 5],  # for 1/2 niftis -> [3.4, 5],
            "HIGH_MAX": [4, 5],  # for 1/2 niftis -> [4, 5],
            "ALPHA": [155, 150],
            "BETA": [180, 170],
            "GRADIENT_RANGE": [115, 255],
            "TRANSPARENCY": 255,
            "LEVELS": 15
        },
        'ARTIFACTS_SOUTH_EAST_ARM': {
            "HIGH_MIN": [3.5, 5],  # for 1/2 niftis -> [3.5, 5],
            "HIGH_MAX": [10, 12],  # for 1/2 niftis -> [10, 12],
            "ALPHA": [225, 220],
            "BETA": [250, 245],
            "GRADIENT_RANGE": [115, 255],
            "TRANSPARENCY": 255,
            "LEVELS": 15
        },
        'ARTIFACTS_SOUTH_WEST_ARM': {
            "HIGH_MIN": [3.5, 7.5],  # for 1/2 niftis -> [3.5, 5],
            "HIGH_MAX": [5, 8],  # for 1/2 niftis -> [5, 8],
            "ALPHA": [295, 290],
            "BETA": [325, 320],
            "GRADIENT_RANGE": [115, 255],
            "TRANSPARENCY": 255,
            "LEVELS": 15
        },
        'ARTIFACTS_NORD_WEST_ARM': {
            "HIGH_MIN": [3.5, 5],  # for 1/2 niftis -> [3.5, 5],
            "HIGH_MAX": [10, 12],  # for 1/2 niftis -> [10, 12],
            "ALPHA": [365, 360],
            "BETA": [395, 390],
            "GRADIENT_RANGE": [115, 255],
            "TRANSPARENCY": 255,
            "LEVELS": 15
        },
        'ARTIFACTS_STRIPES': {
            "INTENESITY": 11,
            "HIGH_MAX": [92, 89],  # for 1/2 niftis -> [92, 89],
            "HIGH_MIN": [25, 20],  # for 1/2 niftis -> [25, 20],
            "DEGREE_FIRST": [308, 215],
            "DEGREE_SECOND": [200, 160],
            "D_DEGREE": 0.2,
            "J": 10,
            "I": 8,

        }
    }
