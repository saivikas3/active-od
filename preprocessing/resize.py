import json
import os
import cv2

#reading the config file
with open("../config.json","r") as config_file:
    config = json.load(config_file)

#dataset directory
dataset_params = config['dataset_params']
annotated_dir = dataset_params['annotated']

#resizing the images
WIDTH = 1216
HEIGHT = 1216


image_list = os.listdir(annotated_dir)


for img_file in image_list:
  if img_file[-4:] == '.jpg': 
    img_path = os.path.join(annotated_dir,img_file)
    img = cv2.imread(img_path)
    resized = cv2.resize(img, (WIDTH,HEIGHT))
    cv2.imwrite(img_path, resized)
