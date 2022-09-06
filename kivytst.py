from kivy.app import App
from kivy.uix.label import Label
import keyboard


def get_text(file_path):
    try:
        with open(f"{file_path}") as w:
            f = w.read()
        return str(f)
    except:
        return "Not found, Sorry, the user has no data entered yet."


class MyApp(App):
    def build(self):
        return Label(text=get_text('test.txt'), color="#DADADA")

    def kill(self):
        return Label(quit())


if keyboard.is_pressed('ctrl'):
    MyApp().run()
    # MyApp().kill()
