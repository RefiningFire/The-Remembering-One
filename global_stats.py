from kivy.uix.screenmanager import ScreenManager, SlideTransition

import decks.starting
import decks.summer
import decks.test
import decks.terraforming

import galaxy_gen

import numpy as np
import ast

stats = {
    'male_baby_count':0,'male_baby_approval':0,
    'female_baby_count':0,'female_baby_approval':0,
    'male_child_count':0,'male_child_approval':0,
    'female_child_count':0,'female_child_approval':0,
    'male_teen_count':0,'male_teen_approval':0,
    'female_teen_count':0,'female_teen_approval':0,

    'male_settler_count':43,'male_settler_approval':50,
    'female_settler_count':43,'female_settler_approval':50,
    'male_farmer_count':5,'male_farmer_approval':50,
    'female_farmer_count':5,'female_farmer_approval':50,
    'male_engineer_count':2,'male_engineer_approval':50,
    'female_engineer_count':2,'female_engineer_approval':50,


    'scrap_metal':100,

    'module_patches':100,

    'habitat_modules':20,'habitat_condition':100,'habitat_space_used':10,

    'greenhouse_modules':10,'greenhouse_condition':100,'greenhouse_space_used':2,'greenhouse_fertility':55,'greenhouse_panels':10,

    'food_reserves':500,'food_storage':1000,'food_production':110,'food_consumption':100,

    'atmosphere_percentage':0,
    'ocean_percentage':0,'arable_percentage':0,

    'year':0,
    'day':1,
    'hour':5,
    'minute':0,
    'age':20,'age_in_earth_days':7300,

    'wake_time':5,'breakfast_start':6,'breakfast_end':7,'council_start':8,'council_end':18,'dinner_start':19,'dinner_end':20,'sleep_time':22,

    'player_name':'John','stamina':20,
    'pc_str':8,'pc_dex':8,'pc_int':8,'pc_wis':8,'pc_con':8,'pc_cha':8,

    'current_card_id':''
}

#galaxy_stats = galaxy_gen.stats_gen()
#print(galaxy_stats)

# This function sets the appropriate data type for card data.
def data_type(data):
    # Check for empty field.
    if data == '': return ast.literal_eval('[]')
    # List.
    elif data[0] == '[':return ast.literal_eval(data)
    # Boolean
    elif data.lower() == 'true': return True
    elif data.lower() == 'false': return False
    # Integer
    elif data[0] in '0123456789' and data[-1]in '0123456789': return int(data)
    # Other: should be string.
    else:return data

def make_deck(deck_file):
    # Import dictionary, and make a list for each line.
    f = [i.strip('\n').replace('"','').split('\t') for i in open(deck_file, "r").readlines()]

    # Create the dictionary.
    d = {}

    # This list will be populated by the card variant id's and used to populate their data.
    ids = []

    # iterate through each row.
    for row in f:
        # Add the card variant sub-dictionaries.
        if row[0] == 'ID':
            for id in row[1:]:
                d.update({id:{}})
                ids.append(id)
            # Set the current section variable as meta_data.
            cur_sec = 'meta_data'

        # If at the space between cards, reset the ids list to prep for a new card type.
        elif row == ['']:
            ids = []

        # Check for the option's tag, and create the sub-dictionary..
        elif row[0] == 'options':
            for i, variant in enumerate(row[1:]):
                # Update the current variant with the options sub-dictionary.
                d[ids[i]].update({'options':{}})
            # set the current section as options.
            cur_sec = 'options'

        # Create each meta_data line.
        elif cur_sec == 'meta_data':
            for i, data in enumerate(row[1:]):
                # Update the current variant with the current meta_data.
                d[ids[i]].update({row[0]:data_type(data)})

        # Check for any opt#, and create the sub-dicitonary.
        elif row[0] == 'opt1' or row[0] == 'opt2' or row[0] == 'opt3' or row[0] == 'opt4' or row[0] == 'opt5':
            for i, variant in enumerate(row[1:]):
                # Check that the card has this option.
                if variant != '':
                    # Update the current variant with the opt# sub-dictionary.
                    d[ids[i]]['options'].update({row[0]:{}})
                    # Update the current opt# text field with the current data.
                    d[ids[i]]['options'][row[0]].update({'text':data_type(variant)})

            # Set the current section as the current opt #.
            cur_sec = row[0]


        else: # Create each option data line.
            for i, data in enumerate(row[1:]):
                if cur_sec in d[ids[i]]['options']:
                    # Update the current opt# with the current data.
                    d[ids[i]]['options'][cur_sec].update({row[0]:data_type(data)})

    return d

sm = ScreenManager(transition=SlideTransition())


main_deck = make_deck('decks/starting.tsv')
main_deck.update(make_deck('decks/greenhouse.tsv'))

all_unused_cards = make_deck('decks/utility.tsv')
#all_unused_cards.update(make_deck('summer_deck.tsv'))


delayed_deck = []



# Create an empty dictionary that will hold all_used_cards.
all_used_cards = {}

# Create the 'on deck' deck, where cards go once selected, but before actually added to the main deck.
to_be_added = {}
