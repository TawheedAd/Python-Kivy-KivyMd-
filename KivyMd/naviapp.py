import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivymd.app import MDApp
from kivy.lang.builder import Builder


kv = """
<DrawerClickableItem@MDNavigationDrawerItem>
<DrawerLableItem@MDNavigationDrawerItem>

MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDTopAppBar:
                    pos_hint:{"top":1}
                    title:"GoGreen"
                    elivation:4
                    left_action_items:[['menu',lambda x:nav_drawer.set_state("open")]]
        MDNavigationDrawer:
            id:nav_drawer
            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    source:"b.png"
                    title:"GoGreen"
                    text: "@GoGreen"
                    spacing:"4dp"
                    padding:22
                MDNavigationDrawerLabel: 
                    text:"Menu"   
                DrawerClickableItem:
                    icon:"gmail"
                    text:"Inbox"    
                DrawerClickableItem:
                    icon:"gmail"
                    text:"Send"     
                DrawerClickableItem:
                    icon:"gmail"
                    text:"Draft"  
                MDNavigationDrawerDivider:       
                          
                MDNavigationDrawerLabel: 
                    text:"Contact"    
                DrawerLableItem:
                    icon:"facebook"
                    text:"Facebook"         
                



"""

class NaviApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        builderr=Builder.load_string(kv)
        return builderr


NaviApp().run()