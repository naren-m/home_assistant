import configparser
config = configparser.ConfigParser()
config.read('config.ini')

print config.get('Paths', 'home_dir')
# print config.get('Paths', 'actions')
