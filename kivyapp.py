import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, DictProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget

import kivyappconfig
import os.path

#Write default ini file if it doesn't exist
if not os.path.isfile('kivyapp.ini'):
    kivyappconfig.setup()

config = kivyappconfig.get_config_parser()
config.read('kivyapp.ini')
#images = []
#for i in range(1,10):
#    images.append(config.get('images', 'image%s' %i,))


class PasswordScreen(Screen):
    appPassword = StringProperty()
    def password_check(self, password):
        config = kivyappconfig.get_config_parser()
        config.read('kivyapp.ini')
        appPassword = config.get('default', 'password', fallback='123')
        if password == appPassword:
            print('success')
            self.manager.current = 'imageScrn'
        else:
            print('incorrect password')


#class MyButton(ButtonBehavior, Image):
    #images = ListProperty([])
    #def __init__(self, **kwargs):
    #    super(MyButton, self).__init__(**kwargs)

        #self.source = images.pop(0)
        #print('Ive been called')
        #self.background_color = 1,1,1,1

class ImageScreen(Screen):
    imageGuess = StringProperty('')
    images = DictProperty({})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 10):
            self.images[i] = config.get('images', 'image%s' %i)
        print(self.images)

    def reset_buttons(self):
        for button in range(1, 10):
            self.ids[str(button)].opacity = 1

    def get_image_source(self, instance):
        instance.source = images[0]
        images.pop[0]


    def image_check(self, instance, id):
        instance.opacity = 0.4
        print('%s button pressed' %id)
        self.imageGuess += id
        if len(self.imageGuess) == 3:
            print('Guess was: ' + self.imageGuess)
            if self.imageGuess == '123':
                self.imageGuess = ''
                #Reset buttons
                for button in range(1, 10):
                    self.ids[str(button)].opacity = 1
                self.manager.current = 'successScrn'
            else:
                self.imageGuess = ''
                #Reset Buttons
                for button in range(1, 10):
                    self.ids[str(button)].opacity = 1
                    
class SuccessScreen(Screen):
    def reset(self):
        passwordField.text = ''
        self.manager.current = 'passwordScrn'

        #reset image buttons
        for button in range(1, 9):
            #print(button)
            self.ids[str(button)].opacity = 1


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file('mykivy.kv')

class MyKivyApp(App):

    def build(self):
        return presentation



MyKivyApp().run()
