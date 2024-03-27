import os

from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivy.app import App
from kivy.uix.widget import Widget


class WidgetExample(GridLayout):
    my_text = StringProperty("Welcome")
    counter = 0
    counter_enable = BooleanProperty(False)
    def on_button_click(self):
        print("Button Clicked")
        if self.counter_enable:
            self.counter+=1
            self.my_text = str(self.counter)
            if str(self.counter)=="20":
                self.my_text="C-TAD"
    def on_toggle_button_state(self,togglebutton):
        print("toggle state  "+togglebutton.state)
        if togglebutton.state == "normal":
            #OFF
            togglebutton.text ="OFF"
            self.counter_enable = False
        else:
            #ON
            togglebutton.text = "ON"
            self.counter_enable = True
    def on_switch_active(self,switch):
        print("Switch : " +str(switch.active))
    # slidertext=StringProperty("Value")
    def on_slider_value(self,slider):
          #self.slidertext=str(int(slider.value))
          #print("slider: " + str(int(slider.value)))
        pass



class TheWidgetApp(App):
    pass

TheWidgetApp().run()