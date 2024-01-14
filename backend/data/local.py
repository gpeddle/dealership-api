import os
import json

from .base import AbstractDataStore
from .config import ConfigFileDescriptor

class LocalDataStore(AbstractDataStore):
    def __init__(self, data_directory):
        super().__init__()
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

        # Read index.json file to get list of config files
        index_file_path = f"{self.data_directory}/index.json"   
        with open(index_file_path, "r") as file:
            index_data = json.load(file)

        # verify that all files in index.json exist
        config_files = []
        for cfg in index_data:
            cfg_path = f"{self.data_directory}/{cfg['filename']}"
            if os.path.isfile(cfg_path):
                version = 'local'
                timestamp = os.path.getmtime(cfg_path)
                descriptor = ConfigFileDescriptor( 
                    cfg['id'],
                    cfg['name'], 
                    cfg['filename'],
                    cfg['path'],
                    cfg['description'],
                    version,
                    cfg['created'],
                    cfg['updated'])
                config_files.append(descriptor)
            else:
                pass
                #print(f'WARNING: Config file {cfg_path} listed in index.json does not exist.')    
        
        return config_files
