from kivy.uix.screenmanager import ScreenManager, SlideTransition

import decks.starting
import decks.summer
import decks.test
import decks.terraforming

import galaxy_gen

import numpy as np

stats = {
    'baby_count':0,'baby_approval':0,
    'child_count':0,'child_approval':0,
    'teen_count':0,'teen_approval':0,
    'settler_count':100,'settler_approval':50,

    'habitat_modules':20,'habitat_condition':100,'habitat_space_used':10,

    'greenhouse_modules':10,'greenhouse_condition':100,'greenhouse_space_used':10,

    'planet_habitability':0,'atmosphere_percentage':40,
    'ocean_percentage':40,'arable_percentage':30,

    'year':0,
    'day':0,
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
