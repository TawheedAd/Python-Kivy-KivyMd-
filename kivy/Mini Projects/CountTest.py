import os

from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivy.app import App

class CountTestHere(GridLayout):
    count=0
    count_enable=False
    my_text=StringProperty("Ready To Start")
    def startme(self,obj):
        if self.count_enable:
            self.count+=1
            self.my_text=str(self.count)
            print(self.count)
    def togglebutton(self,togglebutton):
        print(togglebutton.state)
        if togglebutton.state=="normal":
            togglebutton.text="OFF"
            self.count_enable = False


        else:
            togglebutton.text="ON"
            self.count_enable=True


class CountTest(App):
    pass
CountTest().run()