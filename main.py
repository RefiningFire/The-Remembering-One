from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from kivy.core.window import Window
Window.fullscreen = 'auto'

import decks.starting

class MainScreen(Screen):
    def increase(self):
        app.stats['pops']['settlers'] += 5
        app.stats['pops']['teens'] += 4
        app.stats['pops']['children'] += 3
        app.stats['pops']['babies'] += 2
        app.stats['base_modules']['habitation'] += 1
        app.stats['base_modules']['greenhouse'] -= 1
        app.stats['planet_habitability'] += 7
        app.stats['year'] += 1
        app.stats['day'] += 1

class LoadingScreen(Screen):
    pass

class TheRememberingOneApp(App):
    def build(self):
        app.stats = {
            'pops':{
                'babies':0,
                'children':0,
                'teens':0,
                'settlers':1000,
            },
            'base_modules':{
                'habitation':100,
                'greenhouse':10
            },
            'planet_habitability':0,
            'year':0,
            'day':0

        }

        self.sm = ScreenManager(transition=SlideTransition())
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(LoadingScreen(name='loading'))

        return self.sm

    def load_buttons(self):
        self.__ids = app.sm.get_screen('main').ids

        self.__ids.babies_count.text = str(app.stats['pops']['babies'])
        self.__ids.children_count.text = str(app.stats['pops']['children'])
        self.__ids.teens_count.text = str(app.stats['pops']['teens'])
        self.__ids.settlers_count.text = str(app.stats['pops']['settlers'])

        self.__ids.planet_habitability.text = str(app.stats['planet_habitability'])
        self.__ids.year.text = str(app.stats['year'])
        self.__ids.day.text = str(app.stats['day'])

        self.__ids.habitation.text = str(app.stats['base_modules']['habitation'])
        self.__ids.greenhouse.text = str(app.stats['base_modules']['greenhouse'])


if __name__ == '__main__':
    app = TheRememberingOneApp()
    app.run()
