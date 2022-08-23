class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.__config = self.__read_config()

    def __read_config(self):
        config = {}
        with open(self.config_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=')
                    config[key] = value
        return config

    def __getitem__(self, item):
        return self.get(item)

    def get(self, key, default=None):
        return self.__config.get(key, default)

    def get_bool(self, key, default=None):
        return self.get(key, default) in ['True', 'true', '1']
