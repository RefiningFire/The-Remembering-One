from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen

from kivy.core.window import Window
Window.fullscreen = 'auto'

from main_screen import *
from global_stats import stats, sm


class LoadingScreen(Screen):
    pass

class TheRememberingOneApp(App):
    def build(self):
        app.start_stats = stats

        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(LoadingScreen(name='loading'))

        return sm


if __name__ == '__main__':
    app = TheRememberingOneApp()
    app.run()
