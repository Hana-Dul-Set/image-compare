import os, shutil

def get_duplicated_image_path_list(IMAGE_DIR_PATH):
    duplicated_image_path_list = []
    with open('image_same.csv', 'r') as csv_file:
        image_pairs_list = csv_file.readlines()
        for pair in image_pairs_list:
            image_file_name = pair[:-1].split(',')[1]
            file_path = IMAGE_DIR_PATH + image_file_name
            duplicated_image_path_list.append(file_path)
    return duplicated_image_path_list

def delete_file(file_path):
    if(os.path.exists(file_path)):
        os.remove(file_path)
        print(file_path + " is successfully removed!")
    else:
        print(file_path + " is not valid!")
    return


def delete_duplicated_images(IMAGE_DIR_PATH):
    duplcated_image_path_list = get_duplicated_image_path_list(IMAGE_DIR_PATH)
    if not os.path.isdir('./removed_image'):
        os.mkdir('removed_image')
    for image_path in duplcated_image_path_list:
        if not os.path.isfile(image_path):
            continue
        shutil.copyfile(image_path, './removed_image/' + image_path.split('/')[-1])
        delete_file(image_path)
    return