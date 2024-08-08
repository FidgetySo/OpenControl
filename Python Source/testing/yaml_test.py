import sys
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True

with open('config.yaml') as fp:
    data = yaml.load(fp)

for elem in data:
	if elem['section'] == 'Power':
         elem['EmergencyLevel'] = 1_000
         break  # no need to iterate further
