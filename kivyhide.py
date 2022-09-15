from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
#

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

Config.set('graphics', 'window_state', 'hidden')



class MyApp(App):

    def build(self):
        Window.bordeless = 'True'
        return Button(text='Hello World')

    def on_start(self):
        if self.visible:
            self.root_window.hide()
        self.visible = not self.visible
        # self.root.focus = True

    def do_show(self):
        rootWindow = self.root_window
        rootWindow.show()
        print(self.root_window.focus)

if __name__ in ('__main__'):
    MyApp().run()
    MyApp().visible = True
    MyApp().run()

