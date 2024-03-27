import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class InputFApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation="vertical",spacing=10,padding=250)
        #userinput and login button details
        email = MDTextField(text="Email or Phone No",pos_hint={"center_x":0.5,"center_y":0.5})
        password = MDTextField(text="Password ", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn1 = MDRectangleFlatButton(text="LogIn",pos_hint={"center_x": 0.5, "center_y": 0.5},on_release=self.adddialogbox)



        #merge layout to the elements
        layout.add_widget(email)
        layout.add_widget(password)
        layout.add_widget(btn1)
        return layout

        #Dialogbox on click login function

    def adddialogbox(self,obj):
        # dialogeBox code extended

        #Dialog Box will contain more two buttons at the buttom
        close_btn = MDFlatButton(text="close", on_release=self.close_dialog)
        more_btn = MDFlatButton(text="More", on_release=self.more_btn)

        #Opning Dialog Box & Merging the above buttons
        self.dialog=MDDialog(title="Response ",text="LogIn Sucessfully ",size_hint=(0.7,1),buttons=(close_btn,more_btn))
        self.dialog.open()


    def close_dialog(self,obj):
        self.dialog.dismiss()

    def more_btn(self,obj):
        print("coming Soon")
InputFApp().run()
