import os

from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivy.app import App
from kivy.uix.widget import Widget


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation="lr-bt"
        for i in range(0,100):
            size=dp(100)
            b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
            self.add_widget(b)

# class GridLayoutexample(GridLayout):
#     pass
class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):

    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation="vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     self.add_widget(b1)
    #     self.add_widget(b2)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()