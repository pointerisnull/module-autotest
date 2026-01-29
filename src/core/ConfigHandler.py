import os
from common.constants import *

class ConfigHandler():
    def __init__(self, path="./config/"):
        self.config = "None"
        self.path=path
        self.module=MODULES[0]
        self.has_changed = False

    def create_config(self, name, overwrite=True, module_type=MODULES[0]):
        # Create config file
        directory = os.path.dirname(self.path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        if overwrite:
            # 'w' will overwrite without complaining
            option = 'w'
        else:
            # 'x' will throw FileExistsError if the file is already there
            option = 'x'

        with open(os.path.join(self.path, name) , option) as f:
            f.write(module_type)

        self.config = name
        self.module = module_type

    def set_config(self, name):
        self.config = name
        self.open_config(self.path+self.config)

    def get_config(self):
        return self.config

    def get_module_type(self):
        return self.module

    def get_path(self):
        return self.path

    # Return a list of all configurations present
    def list_configs(self):
        if not os.path.exists(self.path):
            return []
        files = [
            f for f in os.listdir(self.path) 
            if os.path.isfile(os.path.join(self.path, f))
        ]
        return files

    def open_config(self, path):
        print(f"Opening configuration at {path}")
        option = 'r'
        with open(path , option) as f:
            self.module = f.readline()


if __name__ == "__main__":
    conf = ConfigHandler()
    conf.create_config("test2", overwrite=False)
    print(conf.list_configs())