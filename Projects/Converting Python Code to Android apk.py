# Import MDApp from kivymd.app, kivymd.uix.label import MDLabel

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        return MDLabel(text='Using Kivy to convert python code to android apk',
                       halign='center')


if __name__ == '__main__':
    MainApp().run()

'''
In Google Collab create a new notebook

Write code in 'Kivy.txt' one by one in the notebook(code)

NB: Add new code line 

Before running '! buildozer init' upload this file to the notebook

Type 'Y' to continue

Source code will be located in  sample_data/buildozer.spec

Title/ Name of application will be located on line 4
Package name on line 52

Icon filename can be customizable on line 52


On line 39
edit requirements to make it look like:

    requirements = python3, kivy==2.0.0, kivymd, pillow
    

Run next code in 'Kivy.txt' in notebook(code) and type 'Y' to continue.

The apk file will be located in the bin directory,
download file and save to cloud

Finally, open cloud on phone and install apk file.
'''
