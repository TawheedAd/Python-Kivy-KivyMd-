import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


kv = """


"""

class ScreenManagerApp(MDApp):
    def build(self):
        builderr=Builder.load_string(kv)
        return builderr


ScreenManagerApp().run()