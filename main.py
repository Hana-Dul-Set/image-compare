from write_data_utils import *
from compare_utils import *

from delete_utils import *
import os

"""
pip install pillow
pip install tqdm
"""

## 이미지 파일이 있는 경로 입력(맨 뒤에 '/' 필수 입력) ex) './image/'
IMAGE_DIR_PATH = 'PATH'
GET_DUPLICATED_IMAGE_PAIR_OPTION = False
DELETE_OPTION = False

if(GET_DUPLICATED_IMAGE_PAIR_OPTION):
    write_image_pixel_data(IMAGE_DIR_PATH)
    write_same_image_pairs(IMAGE_DIR_PATH)

if(DELETE_OPTION):
    delete_duplicated_images(IMAGE_DIR_PATH)
