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


class PasswordScreen(Screen):
    def password_check(self, password):
        if password == 'password':
            print('success')
            self.manager.current = 'imageScrn'
        else:
            print('incorrect password')

class ImageScreen(Screen):
    imageGuess = StringProperty('')

    def image_check(self, instance):
        self.imageGuess += instance.text
        if len(self.imageGuess) == 3:
            print('Guess was: ' + self.imageGuess)
            if self.imageGuess == '123':
                self.imageGuess = ''
                self.manager.current = 'successScrn'
            else:
                self.imageGuess = ''

class SuccessScreen(Screen):
    def reset(self):
        passwordField.text = ''
        self.manager.current = 'passwordScrn'

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file('mykivy.kv')

class MyKivyApp(App):

    def build(self):
        return presentation

MyKivyApp().run()
