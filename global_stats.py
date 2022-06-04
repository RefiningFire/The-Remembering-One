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


    'scrap_metal':100,

    'module_patches':100,

    'habitat_modules':20,'habitat_condition':100,'habitat_space_used':10,

    'greenhouse_modules':10,'greenhouse_condition':100,'greenhouse_space_used':2,'greenhouse_fertility':55,'greenhouse_panels':10,

    'food_reserves':500,'food_storage':1000,'food_production':110,'food_consumption':100,

    'atmosphere_percentage':0,
    'ocean_percentage':0,'arable_percentage':0,

    'year':0,
    'day':1,
    'hour':0,
    'minute':0,
    'age':20,'age_in_earth_days':7300,

    'wake_time':5,'breakfast_start':6,'breakfast_end':7,'council_start':8,'council_end':18,'dinner_start':19,'dinner_end':20,'sleep_time':22,

    'player_name':'John',

    'current_card_id':''
}

#galaxy_stats = galaxy_gen.stats_gen()
#print(galaxy_stats)



sm = ScreenManager(transition=SlideTransition())

main_deck = decks.starting.deck.copy()

delayed_deck = []

all_unused_cards = decks.terraforming.deck.copy() | decks.summer.deck.copy()

# Create an empty dictionary that will hold all_used_cards.
all_used_cards = {}

# Create the 'on deck' deck, where cards go once selected, but before actually added to the main deck.
to_be_added = {}
