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

import decks.starting as starting

class MainScreen(Screen):
    def increase(self):
        app.stats['pops']['settlers']['count'] += 5
        app.stats['pops']['teens']['count'] += 4
        app.stats['pops']['children']['count'] += 3
        app.stats['pops']['babies']['count'] += 2

        app.stats['pops']['settlers']['approval'] += 5
        app.stats['pops']['teens']['approval'] += 4
        app.stats['pops']['children']['approval'] += 3
        app.stats['pops']['babies']['approval'] += 2

        app.stats['planet_habitability'] += 7
        app.stats['year'] += 1
        app.stats['day'] += 1

        app.stats['base_modules']['habitation'] += 1
        app.stats['base_modules']['greenhouse'] -= 1

    def draw_card(self):
        # Short link to the main screen Float Layout
        self.__parent = app.sm.get_screen('main').ids.pops.parent

        # Short link to the starting deck options.
        self.__options = starting.deck['SD001']['options']


        # Default card dimensions.
        self.__card_width = 900
        self.__card_height = 1200

        # Base of the Card.
        self.current_card = BoxLayout(
                        orientation='vertical',
                        spacing=10,
                        size_hint=(None,None),
                        width=self.__card_width,
                        height=self.__card_height,
                        pos=(self.__parent.width/2-self.__card_width/2,self.__parent.height/2-self.__card_height/2)
        )

        # Card canvas.
        self.current_card.canvas.add(Color(1,1,1,.5))
        self.current_card.canvas.add(Rectangle(pos=self.current_card.pos,size=(self.__card_width,self.__card_height)))

        # Card Title and Text.
        self.title = Label(text=starting.deck['SD001']['name'])
        self.text = Label(text=starting.deck['SD001']['text'])

        # Add Title and Text to card base.
        self.current_card.add_widget(self.title)
        self.current_card.add_widget(self.text)

        # Iterate over each option in the card.
        for each in range(len(starting.deck['SD001']['options'])):
            # Short link to the current option. (Opt1, opt2, etc.)
            self.__current_opt = 'opt' + str(each+1)

            # The base layout of the layout.
            self.option_layout = BoxLayout(orientation='horizontal')

            # The button that selects the current option.
            self.option_btn = Button(
                                text=self.__options[self.__current_opt]['text'],
                                size=self.option_layout.size)

            # The cost and reward layouts.
            self.option_cost_layout = BoxLayout(orientation='vertical')
            self.option_reward_layout = BoxLayout(orientation='vertical')

            # Iterate over each resource cost.
            for i in range(len(self.__options[self.__current_opt]['cost_type'])):
                # Add a label for each cost.
                self.option_cost = Label(
                        text=self.__options[self.__current_opt]['cost_type'][i] + ': ' + str(self.__options[self.__current_opt]['cost_amt'][i]))

                # Add the label to the cost layout.
                self.option_cost_layout.add_widget(self.option_cost)

            # Add all the cost layout to the option layout.
            self.option_layout.add_widget(self.option_cost_layout)

            # Add the option button to the option layout.
            self.option_layout.add_widget(self.option_btn)

            # Iterate over each reward.
            for i in range(len(self.__options[self.__current_opt]['reward'])):
                # Add a label for each reward.
                self.option_reward = Label(
                            text=self.__options[self.__current_opt]['reward'][i] + ': ' + str(self.__options[self.__current_opt]['reward_amt'][i]))

                # Add the label to the reward layout.
                self.option_reward_layout.add_widget(self.option_reward)

            # Add the reward layout to the option layout.
            self.option_layout.add_widget(self.option_reward_layout)

            # Add the option layout to the card base.
            self.current_card.add_widget(self.option_layout)

        # Once all the layout of the card is done, add it to the Float Layout of the main screen.
        self.__parent.add_widget(self.current_card)

    def discard_card(self):
        # Short link to the main screen Float Layout.
        self.__parent = app.sm.get_screen('main').ids.pops.parent

        # Remove the existing current card from the Float Layout.
        self.__parent.remove_widget(self.current_card)



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
                    'approval':50},
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
