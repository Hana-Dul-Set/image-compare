from PIL import Image
import csv
from tqdm import tqdm

def get_pixel_list(IMAGE_DIR_PATH, image_filename):
    image = Image.open(IMAGE_DIR_PATH + image_filename)
    return list(image.getdata())

def get_image_pk_and_size_and_sum(image_data):
    return image_data[0], image_data[1], image_data[2]

def is_same_image_pixel_by_pixel(first_image_pixel_list, second_image_pixel_list):
    image_size = len(first_image_pixel_list)
    for i in range(0, image_size):
        if(first_image_pixel_list[i] != second_image_pixel_list[i]):
            return False
    return True

def get_image_pixel_data_list():
    image_pixel_data_list = []
    with open('image_pixel_data.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            image_pixel_data_list.append([row['img_filename'], row['img_size'], row['img_pixel_sum']])
    return image_pixel_data_list

def write_same_image_pairs(IMAGE_DIR_PATH):

    print("Writing Same Image Pairs Data on image_same.csv")

    image_pixel_data_list = get_image_pixel_data_list()
    image_pixel_data_list_len = len(image_pixel_data_list)

    duplicated_image_cnt = 0

    for i in tqdm(range(image_pixel_data_list_len)):
        image_data = image_pixel_data_list[i]
        image_filename, image_size, image_pixel_sum = get_image_pk_and_size_and_sum(image_data)

        for j in range(i+1, image_pixel_data_list_len):
            target_image_data = image_pixel_data_list[j]
            target_image_filename, target_image_size, target_image_pixel_sum = get_image_pk_and_size_and_sum(target_image_data)
            if( (image_size == target_image_size) and (image_pixel_sum == target_image_pixel_sum) ):
                image_pixel_list = get_pixel_list(IMAGE_DIR_PATH, image_filename)
                target_image_pixel_list = get_pixel_list(IMAGE_DIR_PATH, target_image_filename)

                if(is_same_image_pixel_by_pixel(image_pixel_list, target_image_pixel_list)):
                    with open('image_same.csv', 'a') as csv_file:
                        csv_file.writelines(image_filename + ',' + target_image_filename + '\n')
                    duplicated_image_cnt += 1
    print("There exists " + str(duplicated_image_cnt) + " duplicated image pairs")

