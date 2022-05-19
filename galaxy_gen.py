
import numpy as np
import random


max_sectors = 2
max_planets = 2
max_circumference = 10 # Earth is ~ 250. Unit is 1000 miles.
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

                __west_1 = -1
                __west_2 = -1
                __sw_1 = -1
                __sw_2 = -1
                __south_1 = -1
                __south_2 = -1
                __east_1 = -1
                __east_2 = -1
                __se_1 = -1
                __se_2 = -1
                __wxsw = -1
                __sxsw = -1
                __sxse = -1
                __exse = -1

                # West Regions.
                if __x >= 1:
                    __west_1 = region - 1
                    if __x >= 2:
                        __west_2 = region - 2

                # South Regions.
                if __y >= 1:
                    __south_1 = region - __x_cap
                    if __y >= 2:
                        __south_2 = region - (__x_cap * 2)

                # Southwest Regions.
                if __x >= 1 and __y >= 1:
                    __sw_1 = region - __x_cap - 1
                    if __x >= 2 and __y >= 2:
                        __sw_2 = region - (__x_cap * 2) - 2

                # East Regions.
                if (__x + 2) >= __x_cap:
                    __east_2 = region - (__x_cap - 2)
                    if (__x + 1) >= __x_cap:
                        __east_1 = region - (__x_cap - 1)

                # Southeast Regions.
                if __y >= 1:
                    if (__x + 1) >= __x_cap:
                        __se_1 = region - ((__x_cap * 2) - 1)
                    else:
                        __se_1 = region - (__x_cap - 1)

                    if __y >= 2:
                        if (__x + 2) >= __x_cap:
                            __se_2 = region - ((__x_cap * 3) - 2)
                        else:
                            __se_2 = region - ((__x_cap * 2) - 2)

                # West by Southwest region.
                if __y >= 1:
                    if __x >= 2:
                        __wxsw = region - (__x_cap + 2)
                    elif __y >= 2:
                        __wxsw = region - 2

                # South by Southwest region.
                if __y >= 2:
                    if __x >= 1:
                        __sxsw = region - ((__x_cap * 2) + 1)
                    elif __y >= 3:
                        __sxsw = region - (__x_cap + 1)

                # South by Southeast region.
                if __y >= 2:
                    if (__x + 1) >= __x_cap:
                        __sxse = region - ((__x_cap * 3) - 1)
                    else:
                        __sxse = region - ((__x_cap * 2) - 1)

                # East by Southeast region.
                if __y >= 1:
                    if (__x + 2) >= __x_cap:
                        __exse = region - ((__x_cap * 2) - 2)
                    else:
                        __exse = region - (__x_cap - 2)



                print(f'__y: {__y}')
                print()

                print(f'Region ID: {__region_id}')

                print('Current Region')
                print(f'region: {region}')
                print(__galaxy[sector,planet,region,1])
                print(__galaxy[sector,planet,region,2])
                print(f'__west_1: {__west_1}')
                print(__galaxy[sector,planet,__west_1,1])
                print(__galaxy[sector,planet,__west_1,2])
                print(f'__west_2: {__west_2}')
                print(__galaxy[sector,planet,__west_2,1])
                print(__galaxy[sector,planet,__west_2,2])
                print(f'__sw_1: {__sw_1}')
                print(__galaxy[sector,planet,__sw_1,1])
                print(__galaxy[sector,planet,__sw_1,2])
                print(f'__sw_2: {__sw_2}')
                print(__galaxy[sector,planet,__sw_2,1])
                print(__galaxy[sector,planet,__sw_2,2])
                print(f'__south_1: {__south_1}')
                print(__galaxy[sector,planet,__south_1,1])
                print(__galaxy[sector,planet,__south_1,2])
                print(f'__south_2: {__south_2}')
                print(__galaxy[sector,planet,__south_2,1])
                print(__galaxy[sector,planet,__south_2,2])
                print(f'__east_1: {__east_1}')
                print(__galaxy[sector,planet,__east_1,1])
                print(__galaxy[sector,planet,__east_1,2])
                print(f'__east_2: {__east_2}')
                print(__galaxy[sector,planet,__east_2,1])
                print(__galaxy[sector,planet,__east_2,2])
                print(f'__se_1: {__se_1}')
                print(__galaxy[sector,planet,__se_1,1])
                print(__galaxy[sector,planet,__se_1,2])
                print(f'__se_2: {__se_2}')
                print(__galaxy[sector,planet,__se_2,1])
                print(__galaxy[sector,planet,__se_2,2])
                print(f'__wxsw: {__wxsw}')
                print(__galaxy[sector,planet,__wxsw,1])
                print(__galaxy[sector,planet,__wxsw,2])
                print(f'__sxsw: {__sxsw}')
                print(__galaxy[sector,planet,__sxsw,1])
                print(__galaxy[sector,planet,__sxsw,2])
                print(f'__sxse: {__sxse}')
                print(__galaxy[sector,planet,__sxse,1])
                print(__galaxy[sector,planet,__sxse,2])
                print(f'__exse: {__exse}')
                print(__galaxy[sector,planet,__exse,1])
                print(__galaxy[sector,planet,__exse,2])

                print()
                print()

                __altitude = random.randint(0,14)

                __galaxy[sector,planet,region,3] = random.randint(0,7)
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


    return __galaxy
