
import numpy as np
import random


max_sectors = 2
max_systems = 2 + 1
max_planets = 10 + 1
max_circumference = 8 # Earth is ~ 250. Unit is 1000 miles.
max_regions = (max_circumference * (max_circumference//2)) + 1
max_items = 10


sector_meta_data = max_systems - 1
system_meta_data = max_planets - 1
planet_meta_data = max_regions - 1


def stats_gen():
    # Set up an array to return, filled in with the maximum possible items.
    __galaxy = np.zeros((max_sectors,max_systems,max_planets,max_regions,max_items), dtype='i')

    # Setting this allows us to assign a unique number to each region.
    __planet_id = 1

    # Setting this allows us to assign a unique number to each region.
    __region_id = 1

    # Create a random number of sectors for the galaxy.
    for sector in range(random.randint(1,max_sectors)):

        # For each sector, create a random number of systems.
        for system in range(random.randint(1,max_systems)):

            ### SYSTEM META DATA ###
            ## 0,0: System ID
            ## 0,1:
            ## 0,2: Star Type
            ## 0,3: Star Mass (unit = 1/100th of a Solar Mass)
            ## 0,4:
            ## 0,5:

            # 1 = O is 1 in 3,000,000 (0.00003%), Extremely Luminous Ultraviolet
            # 2 = B is 1 in 800 (0.125%), Very Luminous Blue
            # 3 = A is 1 in 160 (0.625%), White or Bluish-white
            # 4 = F is 1 in 33 (3.03%), White
            # 5 = G is 1 in 13 (7.5%), Yellow. (The Sun)
            # 6 = K is (12%), Orange
            # 7 = M is (76%), Red
            __temp_star_type = random.choices([1,2,3,4,5,6,7],weights=[3,12500,62500,303000,760000,1210000,7645000],k=1)

            __galaxy[sector,system,system_meta_data,0,2] = __temp_star_type[0]

            # Set stellar mass depending on the star type.
            if __galaxy[sector,system,system_meta_data,0,2] == 1:
                __galaxy[sector,system,system_meta_data,0,3] = random.randint(1600,25000)
            elif __galaxy[sector,system,system_meta_data,0,2] == 2:
                __galaxy[sector,system,system_meta_data,0,3] = random.randint(210,1600)
            elif __galaxy[sector,system,system_meta_data,0,2] == 3:
                __galaxy[sector,system,system_meta_data,0,3] = random.randint(140,210)
            elif __galaxy[sector,system,system_meta_data,0,2] == 4:
                __galaxy[sector,system,system_meta_data,0,3] = random.randint(104,140)
            elif __galaxy[sector,system,system_meta_data,0,2] == 5:
                __galaxy[sector,system,system_meta_data,0,3] = random.randint(80,104)
            elif __galaxy[sector,system,system_meta_data,0,2] == 6:
                __galaxy[sector,system,system_meta_data,0,3] = random.randint(45,80)
            elif __galaxy[sector,system,system_meta_data,0,2] == 7:
                __galaxy[sector,system,system_meta_data,0,3] = random.randint(8,45)



            ### END SYSTEM META DATA ###

            # Set this in order to start populating planet distance.
            __previous_planet_distance = 20

            # For each system, create a random number of planets.
            for planet in range(random.randint(1,max_planets)):



                ### PLANET META DATA ###
                ## 0: Planet ID
                ## 1: Distance from Sun (unit = million miles)
                ## 2: Planetary Circumference (unit = 1000 miles)
                ## 3: Planetary Mass (unit = 0.1 MicroSuns (Earth is 30))
                ## 4: Orbital Period (unti =  earth day)
                ## 5: Rotation (unit = earth hour)
                # Set Planet id.
                __galaxy[sector,system,planet,planet_meta_data,0] = __planet_id
                __planet_id += 1

                # Set the max distance.
                __possible_max_distance = __previous_planet_distance * 3

                # Planet's distance from sun, measured in million miles.
                __previous_planet_distance = __galaxy[sector,system,planet,planet_meta_data,1] = random.randint(__previous_planet_distance,__possible_max_distance)

                # Create a random planetary circumference.
                __galaxy[sector,system,planet,planet_meta_data,2] = __circumference = random.randint(1,max_circumference)

                # Set the planet's mass in MicroSuns.
                __galaxy[sector,system,planet,planet_meta_data,3] = random.randint(5,600)




                # The Planet's y coor will always be half the x coor.
                __x_cap = __circumference
                __y_cap = __circumference // 2

                # Multiplying total x by y gives us the number of regions on the planet.
                __region_count = __x_cap * __y_cap

                # These increment after each region is created, in order to assign each reason a unique square on the planet's cartesian system.
                __x = 0
                __y = 0

                # For each planet, create a number of regions that works with the generated circumference.
                for region in range(__region_count):

                    # Assign the current increment of the region id to this region.
                    __galaxy[sector,system,planet,region,0] = __region_id

                    # Assign the current x and y to this region.
                    __galaxy[sector,system,planet,region,1] = __x
                    __galaxy[sector,system,planet,region,2] = __y


                    ### ALTITUDE GENERATION ###

                    # 0 = West1         1 = West2       2 = South1      3 = South2
                    # 4 = Southwest1    5 = Southwest2  6 = East2       7 = East1
                    # 8 = Southeast1    9 = Southeast2  10 = West by SW
                    # 11=South by SW    12=South by SE  13=East by SE
                    __surrounding_regions = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

                    # West Regions.
                    if __x >= 1:
                        __surrounding_regions[0] = region - 1
                        if __x >= 2:
                            __surrounding_regions[1] = region - 2

                    # South Regions.
                    if __y >= 1:
                        __surrounding_regions[2] = region - __x_cap
                        if __y >= 2:
                            __surrounding_regions[3] = region - (__x_cap * 2)

                    # Southwest Regions.
                    if __y >= 1:
                        if __x >= 1:
                            __surrounding_regions[4] = region - __x_cap - 1
                        else:
                            __surrounding_regions[4] = region - 1

                        if __y >= 2:
                            if __x >= 2:
                                __surrounding_regions[5] = region - (__x_cap * 2) - 2
                            else:
                                __surrounding_regions[5] = region - __x_cap - 2

                    # East Regions.
                    if (__x + 2) >= __x_cap:
                        __surrounding_regions[6] = region - (__x_cap - 2)
                        if (__x + 1) >= __x_cap:
                            __surrounding_regions[7] = region - (__x_cap - 1)

                    # Southeast Regions.
                    if __y >= 1:
                        if (__x + 1) >= __x_cap:
                            __surrounding_regions[8] = region - ((__x_cap * 2) - 1)
                        else:
                            __surrounding_regions[8] = region - (__x_cap - 1)

                        if __y >= 2:
                            if (__x + 2) >= __x_cap:
                                __surrounding_regions[9] = region - ((__x_cap * 3) - 2)
                            else:
                                __surrounding_regions[9] = region - ((__x_cap * 2) - 2)

                    # West by Southwest region.
                    if __y >= 1:
                        if __x >= 2:
                            __surrounding_regions[10] = region - (__x_cap + 2)
                        else:
                            __surrounding_regions[10] = region - 2

                    # South by Southwest region.
                    if __y >= 2:
                        if __x >= 1:
                            __surrounding_regions[11] = region - ((__x_cap * 2) + 1)
                        else:
                            __surrounding_regions[11] = region - (__x_cap + 1)

                    # South by Southeast region.
                    if __y >= 2:
                        if (__x + 1) >= __x_cap:
                            __surrounding_regions[12] = region - ((__x_cap * 3) - 1)
                        else:
                            __surrounding_regions[12] = region - ((__x_cap * 2) - 1)

                    # East by Southeast region.
                    if __y >= 1:
                        if (__x + 2) >= __x_cap:
                            __surrounding_regions[13] = region - ((__x_cap * 2) - 2)
                        else:
                            __surrounding_regions[13] = region - (__x_cap - 2)


                    # Set these variables to empty.
                    __surrounding_altitudes = []
                    __potential_count = 0
                    __floor = 0
                    __ceiling = 0

                    # Add each surrouding region's altitude to the list.
                    for each in __surrounding_regions:
                        if each == -1:
                            __potential_count += 1
                        else:
                            __surrounding_altitudes.append(__galaxy[sector,system,planet,each,3])

                    # If there are no surrounding altitudes, set the start at random.
                    if __potential_count == 14:
                        __chosen_altitude = 20
                    else:
                        __chosen_altitude = random.choice(__surrounding_altitudes)

                    # Set a min and max cap on altitude
                    if (__chosen_altitude - __potential_count) < 0:
                        __floor = 1
                        __ceiling = __chosen_altitude + __potential_count
                    elif (__chosen_altitude + __potential_count) > 39:
                        __ceiling = 39
                        __floor = __chosen_altitude - __potential_count
                    # Select a floor and ceiling, with variance greater if there are fewere known surrounding regions.
                    else:
                        __floor = __chosen_altitude - __potential_count
                        __ceiling = __chosen_altitude + __potential_count

                    # The new altitude is somewhere between the lowest and highest possibel.
                    __new_altitude = random.randint(__floor,__ceiling)

                    # Set the Altitude of the new region.
                    __galaxy[sector,system,planet,region,3] = __new_altitude

                    ### END ALTITUDE GENERATION ###




                    __galaxy[sector,system,planet,region,4] = random.randint(0,7)

                    # Make sure we are not yet at the rightmost x column. Increment.
                    if __x != __x_cap - 1:
                        __x += 1

                    # If we have reached the farthest side, reset the x counter and increment the y counter by one.
                    elif __x == __x_cap - 1:
                        __x = 0
                        __y += 1

                    # Increment the region id.
                    __region_id += 1



                ### PRINT PLANET MAP ###
                '''
                print(f'__y_cap: {__y_cap}')
                print(f'__x_cap: {__x_cap}')

                for y in reversed(range(__y_cap)):
                    for x in range(__x_cap):
                        if __galaxy[sector,system,planet,((y * __x_cap) + x),3] <= 9:
                            print('o',end='')
                        elif __galaxy[sector,system,planet,((y * __x_cap) + x),3] <= 19:
                            print('o',end='')
                        elif __galaxy[sector,system,planet,((y * __x_cap) + x),3] <= 29:
                            print('#',end='')
                        elif __galaxy[sector,system,planet,((y * __x_cap) + x),3] <= 35:
                            print('#',end='')
                        else:
                            #print(__galaxy[sector,system,planet,((y * __x_cap) + x),3],end=' ')
                            print('^',end='')
                    print('',end='\n')
                print()
                '''
                ### END PRINT PLANET MAP ###
    return __galaxy
