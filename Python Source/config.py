import ruamel.yaml

class Config:
    def __init__(self, config_path='config.yaml'):
        self.config_path = config_path

        self.yaml = ruamel.yaml.YAML()
        self.yaml.preserve_quotes = True

        self.file = open(self.config_path, 'r+')
        self.yaml_data = self.yaml.load(self.file)

    def write(self, section, label, value):
        for elem in self.yaml_data:
            if elem['section'] == section:
                elem[label] = value
                break
        # test_output = open('output.yaml', 'w+')
        self.file.seek(0)
        self.file.truncate()
        self.yaml.dump(self.yaml_data, self.file)

    def reload(self):
        pass
