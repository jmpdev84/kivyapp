import configparser

def setup():
    config = configparser.ConfigParser()
    config['default'] = {}
    config['default']['passwordTextLabel'] = 'Enter the password'
    config['default']['passwordSubmitText'] = 'Submit'
    config['default']['passwordCancelText'] = 'Cancel'
    config['default']['password'] = 'password123'
    config['default']['successText'] = 'Success! Click here to return to the password screen.'

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
    #The correct image sequence to press (images start counting from top left to bottom right 1-9)
    config['images']['imageAnswer'] = '123'

    with open('kivyapp.ini', 'w') as configfile:
        config.write(configfile)

def get_config_parser():
    return configparser.ConfigParser()
