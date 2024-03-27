import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem,ThreeLineListItem
from kivymd.uix.scrollview import MDScrollView



class ListApp(MDApp):
    def build(self):

        myscrollview=MDScrollView()
        mylist=MDList()
        item1=ThreeLineListItem(text="FUD Owner",secondary_text="Name : Amjid Khan",tertiary_text="Address : Handwara")
        item2=ThreeLineListItem(text="FUD Owner", secondary_text="Name : Aadil Majeed",
                                  tertiary_text="Address : Baramulla")
        item3 = ThreeLineListItem(text="FUD Owner", secondary_text="Name : Danish Bhat",
                                  tertiary_text="Address : Baramulla")

        myscrollview.add_widget(mylist)
        mylist.add_widget(item1)
        mylist.add_widget(item2)
        mylist.add_widget(item3)


        return myscrollview
ListApp().run()