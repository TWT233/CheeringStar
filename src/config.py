import os

import yaml

SRC_DIR = os.path.dirname(os.path.abspath(__file__))  # '/src'
PROJ_DIR = os.path.join(SRC_DIR, '..')  # '/'
CONF_DIR = os.path.join(PROJ_DIR, 'conf')  # '/conf'

# load config file
conf = yaml.load(open(os.path.join(CONF_DIR, 'config.yaml'), encoding='utf-8'), Loader=yaml.FullLoader)


async def save_conf():
    yaml.dump(conf, open(os.path.join(CONF_DIR, 'config.yaml'), 'w', encoding='utf-8'))
