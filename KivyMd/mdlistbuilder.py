import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivymd.app import MDApp
from kivy.lang.builder import Builder

from kivymd.uix.list import ThreeLineIconListItem
prop = """

MDScrollView:
    MDList:
        ThreeLineIconListItem:
            text:"FD Owners"
            secondary_text:"Name : Amjid Ahmad Khan"
            tertiary_text:"Address: Handwara"
            IconLeftWidget:
                icon:"github"   
        ThreeLineIconListItem:
            text:"FD Owners"
            secondary_text:"Name : Aadil Majeed"
            tertiary_text:"Address: Baramulla"
            IconLeftWidget:
                icon:"github"  
        ThreeLineIconListItem:
            text:"FD Owners"
            secondary_text:"Name : Danish Bhat"
            tertiary_text:"Address: Handwara"
            IconLeftWidget:
                icon:"github"    
        ThreeLineIconListItem:
            text:"FD Owners"
            secondary_text:"Name : Naveed Baba"
            tertiary_text:"Address: Sopore"
            IconLeftWidget:
                icon:"github"            
                

               
            
"""

class ListApp(MDApp):
    def build(self):

        builderr=Builder.load_string(prop)
        return builderr
ListApp().run()