import json
import os
import shutil
import numpy as np

#reading the config file
with open("../config.json","r") as config_file:
    config = json.load(config_file)

#seed
seed = config['seed']
np.random.seed(seed)

#dataset directory
dataset_params = config['dataset_params']
DATASET_DIR = dataset_params['dir']

#gathering data
file_list = os.listdir(DATASET_DIR)
DATASET_SIZE = len(file_list)

#select 50 images at random and form a dataset
all_indexes = np.arange(0,645)
img_indexes = np.random.choice(all_indexes,size=50,replace=False)

file_list = np.array(file_list)
selected_images = file_list[img_indexes]

print(len(selected_images))
print(selected_images)

#copy them to a new directory
annotated_dir = dataset_params['annotated']

for f in selected_images:
   src = DATASET_DIR + f
   dest = annotated_dir
   shutil.copy(src,dest)
   print('Copying %s ...' % (src))
