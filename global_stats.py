from kivy.uix.screenmanager import ScreenManager, SlideTransition

import decks.starting
import decks.summer
import decks.test
import decks.terraforming

stats = {
    'babies_count':0,
    'babies_approval':0,
    'children_count':0,
    'children_approval':0,
    'teens_count':0,
    'teens_approval':0,
    'settlers_count':100,
    'settlers_approval':50,
    'habitat_modules':20,
    'habitat_condition':100,
    'habitat_space_used':10,
    'greenhouse_modules':10,
    'greenhouse_condition':100,
    'greenhouse_space_used':10,
    'planet_habitability':0,
    'year':0,
    'day':0,
    'current_card_id':''
}

sm = ScreenManager(transition=SlideTransition())

main_deck = decks.starting.deck.copy()

all_unused_cards = decks.terraforming.deck.copy() | decks.summer.deck.copy()

# Create an empty dictionary that will hold all_used_cards.
all_used_cards = {}

# Create the 'on deck' deck, where cards go once selected, but before actually added to the main deck.
to_be_added = {}
