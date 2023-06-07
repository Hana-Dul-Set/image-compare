from PIL import Image
import os
import csv
from tqdm import tqdm

def get_pixel_sum(pixel_list):
    sum = 0
    for pixel in pixel_list:
        if(type(pixel) == int):
            sum += pixel
            continue

        for rgb in pixel:
            sum += rgb
    return sum

def write_image_pixel_data(IMAGE_DIR_PATH):

    print("Writing Image Pixel Data on image_pixel_data.csv")

    img_filename_list = os.listdir(IMAGE_DIR_PATH)
    if '.DS_Store' in img_filename_list:
        img_filename_list.remove('.DS_Store')

    csv_file = open('image_pixel_data.csv', 'a')
    field_name = ['img_filename', 'img_size', 'img_pixel_sum']
    csv_writer = csv.DictWriter(csv_file, field_name)
    csv_writer.writerow({ 'img_filename': 'img_filename', 'img_size': 'img_size', 'img_pixel_sum': 'img_pixel_sum'})

    for img_filename in tqdm(img_filename_list):
        img = Image.open(IMAGE_DIR_PATH + img_filename)
        img_pixel_list = list(img.getdata())

        img_size = len(img_pixel_list)
        img_pixel_sum = get_pixel_sum(img_pixel_list)
        csv_writer.writerow({ 'img_filename': img_filename, 'img_size': img_size, 'img_pixel_sum': img_pixel_sum})
