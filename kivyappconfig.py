import configparser

def setup():
    config = configparser.ConfigParser()
    config['default'] = {}
    config['default']['password'] = 'password123'

    config['images'] = {}
    config['images']['image1'] = 'circle.png'
    config['images']['image2'] = 'cross.png'
    config['images']['image3'] = 'dots.png'
    config['images']['image4'] = 'hexagon.png'
    config['images']['image5'] = 'hexagons.png'
    config['images']['image6'] = 'rhombus.png'
    config['images']['image7'] = 'square.png'
    config['images']['image8'] = 'triangle.png'
    config['images']['image9'] = 'triforce.png'
    config['images']['randomize'] = 'True'

    with open('kivyapp.ini', 'w') as configfile:
        config.write(configfile)

def get_config_parser():
    return configparser.ConfigParser()
