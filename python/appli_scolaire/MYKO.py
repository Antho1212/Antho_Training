from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MYKO(App):
    def build(self):
        return Builder.load_file("myko.kv")  # Charge le fichier .kv
        

if __name__ == "__main__":
    MYKO().run()
