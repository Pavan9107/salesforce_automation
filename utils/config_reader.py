import yaml

class ConfigReader:
    @staticmethod
    def read_config():
        with open("config.yaml", 'r') as file:
            return yaml.safe_load(file)

