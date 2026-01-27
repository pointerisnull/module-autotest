
class ConfigHandler():
    def __init__(self, path="./config/"):
        self.config = "None"
        self.path=path
        self.has_changed = False

    def create_config(self, name):
        print(f"Created configuration for {name}")
        self.config = name

    def set_config(self, name):
        self.config = name
        self.open_config(self.path+self.config)

    def get_config(self):
        return self.config
    
    def get_path(self):
        return self.path
    
    def open_config(self, path):
        print(f"Opening configuration at {path}")