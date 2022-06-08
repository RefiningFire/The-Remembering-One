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

def opt_data_creation(i):
    if i[4][0] == '[':
        return ast.literal_eval(i[4])
    elif i[4][0] in '0123456789' and i[4][-1]in '0123456789':
        return int(i[4])
    else:
        return i[4]



def make_deck(deck_file):
    f = open(deck_file, "r").readlines()

    f = [i.strip('\n').replace('"','').split('\t') for i in f]

    # Create the dictionary.
    d = {}

    # Set counter to 0.
    n = 0

    # Tracks the number of lines to add. (each card has 64 lines, so after each pass 64 is added to x)
    x = 0
    for i in f:
        # Create the name field.
        if n == 0+x:
            d.update({i[0]:{i[1]:i[2]}})

        # Create the card meta_data
        elif n > 0+x and n <= 8+x:
            if i[2][0] == '[':
                d[i[0]][i[1]] = ast.literal_eval(i[2])
            else:
                d[i[0]][i[1]] = i[2]

            if n == 8+x:
                d[i[0]]['options'] = {}
                d[i[0]]['options']['opt1'] = {}

        # opt1
        elif n >= 9+x and n <= 19+x:
            d[i[0]]['options']['opt1'][i[3]] = opt_data_creation(i)

            if n == 19+x:
                d[i[0]]['options']['opt2'] = {}

        # opt2
        elif n >= 20+x and n <= 30+x:
            d[i[0]]['options']['opt2'][i[3]] = opt_data_creation(i)

            if n == 30+x:
                d[i[0]]['options']['opt3'] = {}

        # opt3
        elif n >= 31+x and n <= 41+x:
            d[i[0]]['options']['opt3'][i[3]] = opt_data_creation(i)

            if n == 41+x:
                d[i[0]]['options']['opt4'] = {}

        # opt4
        elif n>= 42+x and n <= 52+x:
            d[i[0]]['options']['opt4'][i[3]] = opt_data_creation(i)

            if n == 52+x:
                d[i[0]]['options']['opt5'] = {}

        # opt5
        elif n >= 53+x and n <= 63+x:
            d[i[0]]['options']['opt5'][i[3]] = opt_data_creation(i)

        if i == ['']:
            x += 65

        n += 1

    return d



sm = ScreenManager(transition=SlideTransition())

'''
main_deck = decks.starting.deck.copy()
'''

main_deck = make_deck('card_data.tsv')

print(main_deck)
print()

delayed_deck = []

all_unused_cards = decks.terraforming.deck.copy() | decks.summer.deck.copy()

print(all_unused_cards)


# Create an empty dictionary that will hold all_used_cards.
all_used_cards = {}

# Create the 'on deck' deck, where cards go once selected, but before actually added to the main deck.
to_be_added = {}








'''
for i in f[1:]:
    if i[1] not in d[i[0]]:
        d[i[0]][i[1]] = i[2:]
    else:
        d[i[0]][i[1]].extend(i[2:])

print(d)
'''
