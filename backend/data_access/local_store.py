import os
import json
from backend.models.automobile_brand import AutomobileBrand


class LocalStoreDataAccess:
    def __init__(self, data_directory):
        self.data_directory = data_directory  # local path to JSON files

    def read_config(self, config_name):
        file_path = f"{self.data_directory}/{config_name}.json"
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return None

    def write_config(self, config_name, data):
        file_path = f"{self.data_directory}/{config_name}.json"
        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)

    def list_configs(self):
        # List available JSON files in the data directory
        config_files = []
        for filename in os.listdir(self.data_directory):
            if filename.endswith(".json"):
                config_name = os.path.splitext(filename)[0]
                config_files.append(config_name)
        return config_files
