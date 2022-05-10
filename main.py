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
        app.stats['pops']['settlers']['count'] += 5
        app.stats['pops']['teens']['count'] += 4
        app.stats['pops']['children']['count'] += 3
        app.stats['pops']['babies']['count'] += 2
        app.stats['base_modules']['habitation'] += 1
        app.stats['base_modules']['greenhouse'] -= 1
        app.stats['planet_habitability'] += 7
        app.stats['year'] += 1
        app.stats['day'] += 1

        app.stats['pops']['settlers']['approval'] += 5
        app.stats['pops']['teens']['approval'] += 4
        app.stats['pops']['children']['approval'] += 3
        app.stats['pops']['babies']['approval'] += 2

class LoadingScreen(Screen):
    pass

class TheRememberingOneApp(App):
    def build(self):
        app.stats = {
            'pops':{
                'babies':{
                    'count':0,
                    'approval':0},
                'children':{
                    'count':0,
                    'approval':0},
                'teens':{
                    'count':0,
                    'approval':0},
                'settlers':{
                    'count':1000,
                    'approval':0},
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

        self.__ids.babies_count.text = str(app.stats['pops']['babies']['count'])
        self.__ids.children_count.text = str(app.stats['pops']['children']['count'])
        self.__ids.teens_count.text = str(app.stats['pops']['teens']['count'])
        self.__ids.settlers_count.text = str(app.stats['pops']['settlers']['count'])

        self.__ids.babies_fill.size = (app.stats['pops']['babies']['approval'],self.__ids.babies_fill.parent.height)
        self.__ids.children_fill.size = (app.stats['pops']['children']['approval'],self.__ids.children_fill.parent.height)
        self.__ids.teens_fill.size = (app.stats['pops']['teens']['approval'],self.__ids.teens_fill.parent.height)
        self.__ids.settlers_fill.size = (app.stats['pops']['settlers']['approval'],self.__ids.settlers_fill.parent.height)

        self.__ids.planet_habitability.text = str(app.stats['planet_habitability'])
        self.__ids.year.text = str(app.stats['year'])
        self.__ids.day.text = str(app.stats['day'])

        self.__ids.habitation.text = str(app.stats['base_modules']['habitation'])
        self.__ids.greenhouse.text = str(app.stats['base_modules']['greenhouse'])


if __name__ == '__main__':
    app = TheRememberingOneApp()
    app.run()
