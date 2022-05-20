
import numpy as np
import random


max_sectors = 6
max_planets = 6
max_circumference = 80 # Earth is ~ 250. Unit is 1000 miles.
max_regions = max_circumference * (max_circumference//2)
max_items = 5


def stats_gen():
    # Set up an array to return, filled in with the maximum possible items.
    __galaxy = np.zeros((max_sectors,max_planets,max_regions,max_items), dtype='i')

    # Setting this allows us to assign a unique number to each region.
    __region_id = 1

    # Create a random number of sectors for the galaxy.
    for sector in range(random.randint(1,max_sectors)):

        # For each sector, create a random number of planets.
        for planet in range(random.randint(1,max_planets)):

            # Create a random planetary circumference.
            __circumference = random.randint(1,max_circumference)

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
                __galaxy[sector,planet,region,0] = __region_id

                # Assign the current x and y to this region.
                __galaxy[sector,planet,region,1] = __x
                __galaxy[sector,planet,region,2] = __y


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

                __surrounding_heights = 0
                __surrounding_count = 0

                __potential_heights = 0
                __potential_count = 14

                # Iterate over each surrounding region.
                for each in __surrounding_regions:
                    # Do this if the region is populated (Not just a '-1')
                    if each >= 0:
                        # Add the region's height to the surrounding_heights.
                        __surrounding_heights += __galaxy[sector,planet,each,3]
                        __surrounding_count += 1
                        __potential_count -= 1

                # Do this if there is at least one populated surrouding region.
                if __surrounding_count > 0:
                    # Find the average of the surrounding regions heights.
                    __avg_surrounding = __surrounding_heights // __surrounding_count
                # Do this if there are no populated surrounding regions.
                else:
                    __avg_surrounding = 0

                if __avg_surrounding == 0:
                    __avg_floor = 20
                # Make sure the average height is 3 or higher.
                elif __avg_surrounding >= 12:
                    # Floor is a minimum of 1.
                    __avg_floor = __avg_surrounding - 10
                else:
                    # Force floor to be a minimum of 1.
                    __avg_floor = 1

                if __avg_surrounding == 0:
                    __avg_ceiling = 35
                # Make sure the average height is no more than 37.
                elif __avg_surrounding <= 28:
                    # Ceiling is a maximum of 40.
                    __avg_ceiling = __avg_surrounding + 11
                else:
                    # Force ceiling height to 40.
                    __avg_ceiling = 40

                # Do this if there are any non-populated surrounding regions.
                if __potential_count > 0:
                    __potential_height = random.randint((__avg_floor),(__avg_ceiling))
                else:
                    __potential_height = 0

                '''
                if (__avg_surrounding > 3 and __avg_surrounding < 38) or (__potential_height > 3 and __potential_height < 38):
                    __random_factor = random.choice((-2,-1,0,1,2))
                elif __avg_surrounding <= 3 or __potential_height <= 3:
                    __random_factor = random.choice((0,1,2))
                elif __avg_surrounding >= 38 or __potential_height >= 38:
                    __random_factor = random.choice((-2,-1,0))
                '''

                __random_factor = 0
                # Set the Region's height at the average between the populated and non-populated surrounding regions, plus/minus a random number.
                __galaxy[sector,planet,region,3] = ((__avg_surrounding + __potential_height) // 2) + __random_factor


                '''
                print(f'Surrounding Heights: {__surrounding_heights}')
                print(f'Surrounding Count: {__surrounding_count}')
                print(f'Average Surroundings: {__avg_surrounding}')
                print(f'Potential Heights: {__potential_heights}')
                print(f'Potential Count: {__potential_count}')
                print(f'Average Potential: {__potential_height}')
                print(f'New Region Altitude: {__galaxy[sector,planet,region,3]}')
                print(f'')
                print(f'')
                '''




                __galaxy[sector,planet,region,4] = random.randint(0,7)

                # Make sure we are not yet at the rightmost x column. Increment.
                if __x != __x_cap - 1:
                    __x += 1

                # If we have reached the farthest side, reset the x counter and increment the y counter by one.
                elif __x == __x_cap - 1:
                    __x = 0
                    __y += 1

                # Increment the region id.
                __region_id += 1

            print(f'__y_cap: {__y_cap}')
            print(f'__x_cap: {__x_cap}')

            for y in reversed(range(__y_cap)):
                for x in range(__x_cap):
                    if __galaxy[sector,planet,((y * __x_cap) + x),3] <= 9:
                        print('.',end='')
                    elif __galaxy[sector,planet,((y * __x_cap) + x),3] <= 19:
                        print('*',end='')
                    elif __galaxy[sector,planet,((y * __x_cap) + x),3] <= 29:
                        print('n',end='')
                    elif __galaxy[sector,planet,((y * __x_cap) + x),3] <= 35:
                        print('M',end='')
                    else:
                        #print(__galaxy[sector,planet,((y * __x_cap) + x),3],end=' ')
                        print('^',end='')
                print('',end='\n')
            print()

    return __galaxy
