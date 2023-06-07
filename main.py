from write_data_utils import *
from compare_utils import *

"""
pip install pillow
pip install tqdm
"""

## 이미지 파일이 있는 경로 입력(맨 뒤에 '/' 필수 입력) ex) './image/'
IMAGE_DIR_PATH = 'PATH'

write_image_pixel_data(IMAGE_DIR_PATH)
write_same_image_pairs(IMAGE_DIR_PATH)