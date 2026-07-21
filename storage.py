import json

import config


def load_data():
    with open(config.DATA_FILE, "r") as file:
        data = json.load(file)
    return data

def save_data(data):
    with open(config.DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)