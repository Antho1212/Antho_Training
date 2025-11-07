from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

class MyWidget(FloatLayout):
    pass

class MYKO(App):
    def build(self):
        return Builder.load_string("""
FloatLayout:
    Label:
        text: 'Bienvenue dans MYKO'
        size_hint: None, None
        size: 200, 50
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    Button:
        text: 'Quitter'
        size_hint: None, None
        size: 200, 50
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: app.stop()
""")

if __name__ == "__main__":
    MYKO().run()
