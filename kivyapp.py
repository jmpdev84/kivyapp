import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.widget import Widget

import kivyappconfig
import os.path

#Write default ini file if it doesn't exist
if not os.path.isfile('kivyapp.ini'):
    kivyappconfig.setup()

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

class ImageScreen(Screen):
    imageGuess = StringProperty('')

    def reset_buttons(self):
        for button in range(1, 10):
            self.ids[str(button)].opacity = 1

    def image_check(self, instance):
        #print('id is ' + instance.id)
        #instance.parent.ids.lid.text = self.get_id(instance)
        #print(instance.parent.ids.lid.text)
        instance.opacity = 0.5
        #l = Label(id='lbl_1', text='1', font_size='30')
        #instance.add_widget(l)
        #instance.text = "1"
        self.imageGuess += instance.text
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

    def get_id(self,  instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return str(id)

class SuccessScreen(Screen):
    def reset(self):
        passwordField.text = ''
        self.manager.current = 'passwordScrn'

        #reset image buttons
        for button in range(1, 9):
            print(button)
            self.ids[str(button)].opacity = 1


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file('mykivy.kv')

class MyKivyApp(App):

    def build(self):
        return presentation



MyKivyApp().run()
