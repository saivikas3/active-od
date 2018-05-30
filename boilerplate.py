import json

#reading the config file
with open("../config.json","r") as config_file:
    config = json.load(config_file)

#dataset directory
dataset_params = config['dataset_params']
annotated_dir = dataset_params['annotated']


