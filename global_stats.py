from kivy.uix.screenmanager import ScreenManager, SlideTransition

import decks.starting
import decks.summer
import decks.test
import decks.terraforming

import galaxy_gen

import numpy as np

stats = {
    'male_baby_count':0,'male_baby_approval':0,
    'female_baby_count':0,'female_baby_approval':0,
    'male_child_count':0,'male_child_approval':0,
    'female_child_count':0,'female_child_approval':0,
    'male_teen_count':0,'male_teen_approval':0,
    'female_teen_count':0,'female_teen_approval':0,

    'male_settler_count':45,'male_settler_approval':50,
    'female_settler_count':45,'female_settler_approval':50,
    'male_farmer_count':5,'male_farmer_approval':50,
    'female_farmer_count':5,'female_farmer_approval':50,





    'habitat_modules':20,'habitat_condition':100,'habitat_space_used':10,

    'greenhouse_modules':10,'greenhouse_condition':100,'greenhouse_space_used':2,'greenhouse_fertility':100,

    'food_reserves':500,'food_storage':1000,'food_production':200,'food_consumption':100,

    'atmosphere_percentage':0,
    'ocean_percentage':0,'arable_percentage':0,

    'year':0,
    'day':1,
    'hour':0,

    'current_card_id':''
}

#galaxy_stats = galaxy_gen.stats_gen()
#print(galaxy_stats)



sm = ScreenManager(transition=SlideTransition())

main_deck = decks.starting.deck.copy()

all_unused_cards = decks.terraforming.deck.copy() | decks.summer.deck.copy()

# Create an empty dictionary that will hold all_used_cards.
all_used_cards = {}

# Create the 'on deck' deck, where cards go once selected, but before actually added to the main deck.
to_be_added = {}
