from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
import keyboard
from kivy.core.window import Window

Config.set('graphics', 'window_state', 'hidden')


def get_text(file_path):
    try:
        with open(f"{file_path}") as w:
            f = w.read()
        return str(f)
    except:
        return "Not found, Sorry, the user has no data entered yet."


class MyApp(App):
    def build(self):
        # Window.bordeless = 'True'
        return Label(text=display('test.txt'), color="#DADADA")


MyApp().run()