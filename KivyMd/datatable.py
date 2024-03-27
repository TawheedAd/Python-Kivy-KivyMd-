import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.anchorlayout import MDAnchorLayout


class tab(MDApp):
    def build(self):
       layout=MDAnchorLayout()
       mytable=MDDataTable(
           size_hint=(0.6,0.7),
           check=True,
           use_pagination=True,
           column_data=[
               ("No",dp(30)),
               ("Price",dp(30)),
               ("Name",dp(30)),
           ],
           row_data=[
               ("1", "250","Momo"),
               ("2", "250", "Momo"),
               ("3", "250", "Momo"),
               ("4", "250", "Momo"),
               ("5", "250", "Momo"),
               ("6", "250", "Momo"),
          ]




       )
       layout.add_widget(mytable)
       return layout
tab().run()