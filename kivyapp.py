import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, DictProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
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

#Read the app settings from the ini file
config = kivyappconfig.get_config_parser()
config.read('kivyapp.ini')

class PasswordScreen(Screen):
    settings = DictProperty({})
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings['password'] = config.get('default', 'password', fallback='123')
        self.settings['passwordTextLabel'] = config.get('default', 'passwordTextLabel')
        self.settings['passwordSubmitText'] = config.get('default', 'passwordSubmitText')
        self.settings['passwordCancelText'] = config.get('default', 'passwordCancelText')

    def password_check(self, password):
        appPassword = self.settings['password']
        if password == appPassword:
            print('success')
            self.manager.current = 'imageScrn'
        else:
            print('incorrect password')
            self.background_color = (1,1,1,1)
            #print(self.ids['passwordField'].ba)

class ImageScreen(Screen):
    imageGuess = StringProperty('')
    imageAnswer = StringProperty('')
    images = DictProperty({})
    counter = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Set up images fomr ini file
        for i in range(1, 10):
            self.images[i] = config.get('images', 'image%s' %i)

        #Set up image guess length
            self.imageAnswer = config.get('images', 'imageAnswer')

    def image_check(self, instance, id):
        instance.opacity = 0.4
        print('%s button pressed' %id)
        self.imageGuess += id
        self.counter += 1
        instance.text = str(self.counter)
        if len(self.imageGuess) == len(self.imageAnswer):
            print('Guess was: ' + self.imageGuess)
            if self.imageGuess == self.imageAnswer:
                self.imageGuess = ''
                #Reset button presses
                for button in range(1, 10):
                    self.ids[str(button)].opacity = 1
                    self.counter = 0
                self.manager.current = 'successScrn'
            else:
                self.imageGuess = ''
                #Reset button presses
                for button in range(1, 10):
                    self.ids[str(button)].opacity = 1
                    self.counter = 0

class SuccessScreen(Screen):
    successText = StringProperty('')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Set up success screen text
        self.successText = config.get('default', 'successText')

    def reset(self):
        passwordField.text = ''
        self.manager.current = 'passwordScrn'

        #reset image buttons
        for button in range(1, 9):
            #print(button)
            self.ids[str(button)].opacity = 1


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_string('''
<Image>:
    center_y: self.parent.center_y
    center_x: self.parent.center_x
    size: 128, 128
    allow_stretch: True

<Label>:
    font_size: 30

ScreenManagement:
    PasswordScreen:
    ImageScreen:
    SuccessScreen:

<PasswordScreen>:
    name: 'passwordScrn'
    id: layoutId
    FloatLayout:
        TextInput:
            id: passwordField
            pos_hint:{"center_x": 0.5, "center_y": 0.5}
            size_hint: None, .08
            width: 400
            font_size: 32
            multiline: False
            password: True
            hint_text: root.settings['passwordTextLabel']
            on_text_validate: layoutId.password_check(passwordField.text)
        Button:
            text: root.settings['passwordSubmitText']
            pos_hint: {"center_x": .4, 'center_y': .4}
            on_press: layoutId.password_check(passwordField.text)
            size_hint: 0.2, 0.08

        Button:
            text: root.settings['passwordCancelText']
            pos_hint: {"center_x": .6, 'center_y': .4}
            on_press: passwordField.text = ''
            size_hint: 0.2, 0.08

<ImageScreen>:
    name: 'imageScrn'
    id: imageScrnId

    GridLayout:
        rows: 3
        padding: 10
        spacing: 10

        BoxLayout:
            spacing: 10
            Button:
                id: 1
                font_size: 50
                background_normal: ''
                on_press: imageScrnId.image_check(self, '1')
                Image:
                    source: root.images[1]
            Button:
                id: 2
                font_size: 50
                background_normal: ''
                on_press: imageScrnId.image_check(self, '2')
                Image:
                    source: root.images[2]
            Button:
                id: 3
                font_size: 50
                background_normal: ''
                on_press: imageScrnId.image_check(self, '3')
                Image:
                    source: root.images[3]
        BoxLayout:
            spacing: 10
            Button:
                id: 4
                font_size: 50
                background_normal: ''
                on_press: imageScrnId.image_check(self, '4')
                Image:
                    source: root.images[4]
            Button:
                id: 5
                font_size: 50
                background_normal: ''
                on_press: imageScrnId.image_check(self, '5')
                Image:
                    source: root.images[5]
            Button:
                id: 6
                font_size: 50
                background_normal: ''
                on_press: imageScrnId.image_check(self, '6')
                Image:
                    source: root.images[6]
        BoxLayout:
            spacing: 10
            Button:
                id: 7
                font_size: 50
                background_normal: ''
                on_press: imageScrnId.image_check(self, '7')
                Image:
                    source: root.images[7]
            Button:
                id: 8
                font_size: 50
                background_normal: ''
                on_press: imageScrnId.image_check(self, '8')
                Image:
                    source: root.images[8]
            Button:
                id: 9
                font_size: 50
                background_normal: ''
                on_press: imageScrnId.image_check(self, '9')
                Image:
                    source: root.images[9]

<SuccessScreen>:
    name: 'successScrn'
    id: successScreen
    FloatLayout:
        Button:
            on_press: app.root.get_screen('passwordScrn').ids.passwordField.text = ''
            on_release: app.root.current = 'passwordScrn'
            text: root.successText
            font_size: 30
''')

class MyKivyApp(App):

    def build(self):
        return presentation

MyKivyApp().run()
