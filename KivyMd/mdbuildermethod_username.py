import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
import kivy
from kivymd.app import MDApp
from  kivy.lang.builder import Builder
from kivymd.uix.screen import Screen

style = """
MDBoxLayout:
    orientation:"vertical"
    padding:300
    spacing:10
    MDTextField:
        pos_hint:{"center_x":0.5,"center_y":0.5}
        hint_text:"Enter username or Email"
        helper_text:"username must be unique"
        helper_text_mode:"on_focus"
        icon_left:"account"
        size_hint_x:None
        width:300
    MDTextField:
        pos_hint:{"center_x":0.5,"center_y":0.5}
        hint_text:"Enter Your Password "
        helper_text:"Password must be unique"
        helper_text_mode:"on_focus"
        icon_left:"lock-off"
        size_hint_x:None
        width:300
            
    MDRectangleFlatButton:
        pos_hint:{"center_x":0.5,"center_y":0.5}
        text:"logIn"
  

"""


class InputFApp(MDApp):
    def build(self):
        scrn = Screen()
        bldr = Builder.load_string(style)
        scrn.add_widget(bldr)
        return scrn
InputFApp().run()