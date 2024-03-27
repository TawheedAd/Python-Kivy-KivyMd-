import os

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivy.app import App
class maincode(BoxLayout):
    text_input_str=StringProperty("hi")
    def on_text_validate(self,TextInput):
        self.text_input_str=TextInput.text



class TextInputApp(App):
    pass
TextInputApp().run()