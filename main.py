from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from kivy.graphics import Color, Rectangle

from kivy.core.window import Window
Window.fullscreen = 'auto'

import random
import math

import decks.starting
import decks.summer
import decks.test
import decks.terraforming

from main_screen import *
from global_stats import stats, sm


'''
test = list(main_deck.items())
print(test[0][1])
'''



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
