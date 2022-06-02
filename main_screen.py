from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.graphics import Color, Rectangle

import random
import math

from global_stats import *


class MainScreen(Screen):
    # Increasing the stat.
    def increase(self):
        #stats['settler_count'] += 5
        stats['teen_count'] += 4
        stats['child_count'] += 3
        #stats['baby_count'] += 2

        #stats['settler_approval'] += 5
        stats['teen_approval'] += 4
        stats['child_approval'] += 3
        #stats['baby_approval'] += 2

        stats['planet_habitability'] += 7
        stats['year'] += 1
        stats['day'] += 1
        stats['hour'] += 1

        stats['habitat_modules'] += 0

        stats['ocean_percentage'] += 1
        stats['arable_percentage'] += 1
        stats['atmosphere_percentage'] += 1

        # Habitat free space is the number of pops divided by 10, rounded up.
        stats['habitat_space_used']=math.ceil((
                            stats['settler_count'] +
                            stats['teen_count'] + stats['child_count'] + stats['baby_count']) / 10)

        stats['greenhouse_space_used'] -= 1

        #print(galaxy_stats[1,0,0,3]) # Planet 1, x 0, y 0, item 3

    # Draw a card from the main deck, and display it on the Screen.
    def draw_card(self):
        # Set iter and selected card variables
        self.__selected_card = random.randint(0,len(main_deck)-1)
        self.__card_draw_iter = 0

        # Iterate through the main deck until the randomly selected number is found.
        for card in main_deck:
            if self.__card_draw_iter == self.__selected_card:
                # Set drawn card id.
                stats['current_card_id'] = card
                break
            self.__card_draw_iter += 1

        # Short link to the main screen Float Layout
        self.__parent = sm.get_screen('main').ids.pops.parent

        # Short link to the card's options.
        self.__options = main_deck[stats['current_card_id']]['options']

        # Default card dimensions.
        self.__card_width = 900
        self.__card_height = 1200

        # Base of the Card.
        self.current_card = BoxLayout(
                            orientation='vertical', spacing=10,
                            size_hint=(None,None),
                            width=self.__card_width,height=self.__card_height,
                            pos=(self.__parent.width/2-self.__card_width/2,self.__parent.height/2-self.__card_height/2))

        # Card canvas.
        self.current_card.canvas.add(Color(1,1,1,.5))
        self.current_card.canvas.add(Rectangle(pos=self.current_card.pos,size=(self.__card_width,self.__card_height)))

        # Card Title, and background.
        self.title = Label(text=main_deck[stats['current_card_id']]['name'],font_size=80,size_hint=(1,.3))

        with self.title.canvas.before:
            Color(.4,.4,.4)
            self.title.rect = Rectangle(pos=self.title.pos, size=self.title.size)

        # Card Text and background.
        self.text = Label(text=main_deck[stats['current_card_id']]['text'])

        with self.text.canvas.before:
            Color(.4,.4,.4)
            self.text.rect = Rectangle(pos=self.text.pos, size=self.text.size)

        # Add Title to card base, update its pos and size.
        self.current_card.add_widget(self.title)
        self.title.bind(pos=update_rect,size=update_rect)

        # Add Text to card base, update its pos and size.
        self.current_card.add_widget(self.text)
        self.text.bind(pos=update_rect,size=update_rect)

        # Iterate over each option in the card.
        for each in range(len(self.__options)):
            # Short link to the current option. (Opt1, opt2, etc.)
            self.__cur_opt = 'opt' + str(each+1)

            self.__display_option = True

            # First check if the option has any requirements.
            if 'req_type' in self.__options[self.__cur_opt]:

                for i in range(len(self.__options[self.__cur_opt]['req_type'])):

                    # For each requirement, check if that stat is below the required amount. If so, do not display the option.
                    if stats[self.__options[self.__cur_opt]['req_type'][i]] < self.__options[self.__cur_opt]['req_amt'][i]:
                        self.__display_option = False

            # If there are no requirements, or if all requirements are met, display the option.
            if self.__display_option == True:
                self.add_option(self.__options,self.__cur_opt,each)

        # Once all the layout of the card is done, add it to the Float Layout of the main screen.
        self.__parent.add_widget(self.current_card)

    # Adds an option to the card display.
    def add_option(self, options,cur_opt,each):
        self.__options = options
        self.__cur_opt = cur_opt

        # The base layout of the layout.
        self.option_layout = BoxLayout(
                                orientation='horizontal',
                                size_hint=(1,.2))

        # Build the background for the option.
        with self.option_layout.canvas:
            Color(.4, .4, .4)
            self.option_layout.rect = Rectangle(pos=self.option_layout.pos, size=self.option_layout.size)

        # The button that selects the current option.
        self.option_btn = Button(
                            text=(f'{self.__options[self.__cur_opt]["text"]}\nHours: {self.__options[self.__cur_opt]["time"]}'),
                            size_hint=(1.3,1))

        # The cost and reward layouts.
        self.option_cost_layout = BoxLayout(orientation='vertical')
        self.option_reward_layout = BoxLayout(orientation='vertical')

        # Clear the type and amount holders. They will be used when binding the option button.
        self.cur_opt_cost_type = []
        self.cur_opt_cost_type_text = []
        self.cur_opt_cost_amt = []
        self.cur_opt_cost_amt_text = []
        self.cur_opt_rwd_type = []
        self.cur_opt_rwd_amt = []
        self.cur_opt_new_cards = []

        # Iterate over each resource cost.
        for i in range(len(self.__options[self.__cur_opt]['cost_type'])):

            # The current cost type.
            self.__cost_type = self.__options[self.__cur_opt]['cost_type'][i]
            # The current cost amount.
            self.__cost_amt = self.__options[self.__cur_opt]['cost_amt'][i]

            # Convert the background ID's and numbers into readable text.
            self.__type_text,self.__amt_text  = self.type_text_select(self.__cost_type,self.__cost_amt,'cost')

            # Save the option type and amt to the button so they can change.
            self.cur_opt_cost_type.append(self.__cost_type)
            self.cur_opt_cost_amt.append(self.__cost_amt)

            # Add a label for each cost.
            self.option_cost = Label(
                        text=self.__type_text + ': ' + self.__amt_text)

            # Add the label to the cost layout.
            self.option_cost_layout.add_widget(self.option_cost)

        # Set types and amounts of cost for each option.
        if each == 0:
            self.opt1_cost_types = self.cur_opt_cost_type
            self.opt1_cost_amt = self.cur_opt_cost_amt
        elif each == 1:
            self.opt2_cost_types = self.cur_opt_cost_type
            self.opt2_cost_amt = self.cur_opt_cost_amt
        elif each == 2:
            self.opt3_cost_types = self.cur_opt_cost_type
            self.opt3_cost_amt = self.cur_opt_cost_amt

        # Iterate over each reward.
        for i in range(len(self.__options[self.__cur_opt]['rwd_type'])):

            # The current reward type.
            self.__rwd_type = self.__options[self.__cur_opt]['rwd_type'][i]
            # The current reward amount.
            self.__rwd_amt = self.__options[self.__cur_opt]['rwd_amt'][i]

            # Convert the background ID's and numbers into readable text.
            self.__type_text,self.__amt_text  = self.type_text_select(self.__rwd_type,self.__rwd_amt,'rwd')

            # Save the reward type and amt to the button so they can change.
            self.cur_opt_rwd_type.append(self.__rwd_type)
            self.cur_opt_rwd_amt.append(self.__rwd_amt)

            # Add a label for each reward.
            self.option_reward = Label(
                        text=self.__type_text + ': ' + self.__amt_text)

            # Add the label to the reward layout.
            self.option_reward_layout.add_widget(self.option_reward)

        for i in range(len(self.__options[self.__cur_opt]['new_cards'])):
            # The current option's new card.
            self.__new_card = self.__options[self.__cur_opt]['new_cards'][i]

            # Save the new cards to the button so it can change.
            self.cur_opt_new_cards.append(self.__new_card)

        # Set types and amounts of reward for each option.
        if each == 0:
            self.opt1_rwd_types = self.cur_opt_rwd_type
            self.opt1_rwd_amt = self.cur_opt_rwd_amt
            self.opt1_new_cards = self.cur_opt_new_cards
        elif each == 1:
            self.opt2_rwd_types = self.cur_opt_rwd_type
            self.opt2_rwd_amt = self.cur_opt_rwd_amt
            self.opt2_new_cards = self.cur_opt_new_cards
        elif each == 2:
            self.opt3_rwd_types = self.cur_opt_rwd_type
            self.opt3_rwd_amt = self.cur_opt_rwd_amt
            self.opt3_new_cards = self.cur_opt_new_cards


        # Bind the cost and rewards to the option button.
        if each == 0:
            self.option_btn.bind(on_press=self.opt1_select)
        elif each == 1:
            self.option_btn.bind(on_press=self.opt2_select)
        elif each == 2:
            self.option_btn.bind(on_press=self.opt3_select)

        # Add all the cost layout to the option layout.
        self.option_layout.add_widget(self.option_cost_layout)

        # Add the option button to the option layout.
        self.option_layout.add_widget(self.option_btn)

        # Add the reward layout to the option layout.
        self.option_layout.add_widget(self.option_reward_layout)

        # Update the position and size of the option background.
        self.option_layout.bind(pos=update_rect,size=update_rect)

        # Add the option layout to the card base.
        self.current_card.add_widget(self.option_layout)

    # Removes a card from the screen, and from the Main Deck.
    def discard_card(self):
        # Short link to the main screen Float Layout.
        self.__parent = sm.get_screen('main').ids.pops.parent

        # Remove the existing current card from the Float Layout.
        self.__parent.remove_widget(self.current_card)

        # If the card is unique, remove it from play.
        if main_deck[stats['current_card_id']]['unique'] == True:
            # Copy this card to the all_used_cards pool.
            all_used_cards[stats['current_card_id']] = main_deck[stats['current_card_id']]

        # Remove this card from the main deck.
        main_deck.pop(stats['current_card_id'])

    # Adds a card to the Main Deck.
    def add_card(self,new_id):
        self.__cards_to_be_added = []

        # Search for the new_id in the unused cards.
        for card in all_unused_cards:
            if new_id in card:
                self.__cards_to_be_added.append(card)

        for card in self.__cards_to_be_added:
            # Add new card to main_deck.
            main_deck[card] = all_unused_cards[card]

            # If the card is unique, remove it from the all_unused_cards pool.
            if main_deck[card]['unique'] == True:
                # Remove the new card from the all_unused_cards pool.
                all_unused_cards.pop(card)

    # Each options selection iterates through the items in the options button and updates the stats.
    def opt1_select(self,instance):
        print(self.opt1_cost_amt)
        for item in range(len(self.opt1_cost_types)):
            stats[self.opt1_cost_types[item]] += self.opt1_cost_amt[item]
        for item in range(len(self.opt1_rwd_types)):
            stats[self.opt1_rwd_types[item]] += self.opt1_rwd_amt[item]
        for card in self.opt1_new_cards:
            self.add_card(card)
        self.load_buttons()
        self.discard_card()
    def opt2_select(self,instance):
        for item in range(len(self.opt2_cost_types)):
            stats[self.opt2_cost_types[item]] += self.opt2_cost_amt[item]
        for item in range(len(self.opt2_rwd_types)):
            stats[self.opt2_rwd_types[item]] += self.opt2_rwd_amt[item]
        for card in self.opt2_new_cards:
            self.add_card(card)
        self.load_buttons()
        self.discard_card()
    def opt3_select(self,instance):
        for item in range(len(self.opt3_cost_types)):
            stats[self.opt3_cost_types[item]] += self.opt3_cost_amt[item]
        for item in range(len(self.opt3_rwd_types)):
            stats[self.opt3_rwd_types[item]] += self.opt3_rwd_amt[item]
        for card in self.opt3_new_cards:
            self.add_card(card)
        self.load_buttons()
        self.discard_card()

    # Update the text of all buttons and labels.
    def load_buttons(self):
        self.__ids = sm.get_screen('main').ids

        self.__ids.baby_count.text = str(stats['baby_count'])
        self.__ids.child_count.text = str(stats['child_count'])
        self.__ids.teen_count.text = str(stats['teen_count'])
        self.__ids.settler_count.text = str(stats['settler_count'])

        self.__ids.baby_fill.size = (stats['baby_approval'],self.__ids.baby_fill.parent.height)
        self.__ids.child_fill.size = (stats['child_approval'],self.__ids.child_fill.parent.height)
        self.__ids.teen_fill.size = (stats['teen_approval'],self.__ids.teen_fill.parent.height)
        self.__ids.settler_fill.size = (stats['settler_approval'],self.__ids.settler_fill.parent.height)

        self.__ids.planet_habitability.text = str(stats['planet_habitability']) + '%'
        self.__ids.year.text = str(stats['year'])
        self.__ids.day.text = str(stats['day'])
        self.__ids.hour.text = str(stats['hour'])

        self.__ids.surface_percentage.text = str(int(stats['ocean_percentage'] * 1.408450704225352)) + '%'
        self.__ids.atmosphere_percentage.text = str(stats['atmosphere_percentage']) + '%'
        self.__ids.habitat_modules.text = str(stats['habitat_space_used']) + '/' + str(stats['habitat_modules'])
        self.__ids.greenhouse_modules.text = str(stats['greenhouse_space_used']) + '/' + str(stats['greenhouse_modules'])

        self.__ids.ocean_fill.size = stats['ocean_percentage'], self.__ids.ocean_fill.parent.height
        self.__ids.arable_fill.size = stats['arable_percentage'], self.__ids.arable_fill.parent.height
        self.__ids.atmosphere_fill.size = stats['atmosphere_percentage'], self.__ids.atmosphere_fill.parent.height
        self.__ids.habitat_fill.size = (stats['habitat_condition'],self.__ids.habitat_fill.parent.height)
        self.__ids.greenhouse_fill.size = (stats['greenhouse_condition'],self.__ids.greenhouse_fill.parent.height)

    # Converts the type and amount into readable text forms.
    def type_text_select(self,type,amt,cost_rwd):

        # Remove any Underscores.
        self.__temp = type.replace('_',' ')

        # Capitalize each word.
        self.__type_text = self.__temp.title()

        # Set the unit, v if a cost, ^ if a reward, and E in any other case.
        self.__unit = '- ' if cost_rwd == 'cost' else '+' if cost_rwd == 'rwd' else 'Error'

        # Set the amount text depending on what percentage of the existing stat is being changed.
        if stats[type] == 0:
            self.__amt_text = 'N/A'
        elif amt/stats[type] > 1:
            self.__amt_text = self.__unit * 5
        elif amt/stats[type] > .60 and amt / stats[type] <= 1:
            self.__amt_text = self.__unit * 4
        elif amt/stats[type] > .30 and amt / stats[type] <= .60:
            self.__amt_text = self.__unit * 3
        elif amt/stats[type] > .10 and amt / stats[type] <= .30:
            self.__amt_text = self.__unit * 2
        elif amt/stats[type] > 0 and amt / stats[type] <= .10:
            self.__amt_text = self.__unit * 1
        else:
            self.__amt_text = 'NONE'

        return self.__type_text, self.__amt_text

# General function for updating a canvas after it has been added to another widget.
def update_rect(instance, value):
    instance.rect.pos = instance.pos
    instance.rect.size = instance.size
