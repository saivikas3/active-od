import json
import os
import cv2

#reading the config file
with open("../config.json","r") as config_file:
    config = json.load(config_file)

#dataset directory
dataset_params = config['dataset_params']
annotated_dir = dataset_params['annotated']

#divide each image into a 2x2 grid and crop

crop_width = 608
crop_height = 608


#image_list = os.listdir(annotated_dir)
image_dir = annotated_dir

image_list = os.listdir(image_dir)

for img_file in image_list:
  if img_file[-4:] == '.jpg':
    
    print('Processing: %s'  % (img_file))
    img_path = os.path.join(image_dir,img_file)
    img = cv2.imread(img_path)
    
    print(img.shape)
    img_top_left = img[:crop_width,:crop_height]
    img_top_right = img[crop_width:,:crop_height]
    img_bottom_left = img[:crop_width,crop_height:]
    img_bottom_right = img[crop_width:,crop_height:]

    img_top_left_file = img_path[:-4] + '_1' + '.jpg'
    img_top_right_file = img_path[:-4] + '_2' + '.jpg'
    img_bottom_left_file = img_path[:-4] + '_3' + '.jpg'
    img_bottom_right_file = img_path[:-4] + '_4' + '.jpg'


    cv2.imwrite(os.path.join(image_dir,img_top_left_file), img_top_left)
    cv2.imwrite(os.path.join(image_dir,img_top_right_file), img_top_right)
    cv2.imwrite(os.path.join(image_dir,img_bottom_left_file), img_bottom_left)
    cv2.imwrite(os.path.join(image_dir,img_bottom_right_file), img_bottom_right)

