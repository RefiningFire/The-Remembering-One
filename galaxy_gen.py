
import numpy as np
import random


max_sectors = 4
max_systems = 4 + 1
max_planets = 10 + 1
max_circumference = 300 # Earth is ~ 250. Unit is 100 miles.
max_regions = ((max_circumference*15) * ((max_circumference*15)//2)) + 1
max_items = 12


sector_meta_data = max_systems - 1
system_meta_data = max_planets - 1
planet_meta_data = max_regions - 1


__solar_mass = 1.98847 * (10**30) # Kilograms
__solar_radius = 6.957 * (10**8) # Meters
__solar_luminosity = 3.828 * (10**26) # Watts

__stefan_boltzmann = 5.670374419 * (10**-8) # Watts per sq Meter


# Set up an array to return, filled in with the maximum possible items.
__galaxy = np.zeros((max_sectors,max_systems,max_planets,max_regions,max_items))


def stats_gen():


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
            ## 0,2: Stellar Type
            ## 0,3: Stellar Mass (unit = 1 kg)
            ## 0,4: Stellar Luminosity (unit = 1 Watt)
            ## 0,5: Stellar Radius (unit = 1 Meter)
            ## 0,6: Stellar Temperature

            # 1 = O is 1 in 3,000,000 (0.00003%), Extremely Luminous Ultraviolet
            # 2 = B is 1 in 800 (0.125%), Very Luminous Blue
            # 3 = A is 1 in 160 (0.625%), White or Bluish-white
            # 4 = F is 1 in 33 (3.03%), White
            # 5 = G is 1 in 13 (7.5%), Yellow. (The Sun)
            # 6 = K is (12%), Orange
            # 7 = M is (76%), Red
            __temp_star_type = random.choices([1,2,3,4,5,6,7],weights=[3,12500,62500,303000,760000,1210000,7645000],k=1)

            __galaxy[sector,system,system_meta_data,0,2] = __temp_star_type[0]

            # Set stellar stats depending on the star type.
            if __galaxy[sector,system,system_meta_data,0,2] == 1:
                # Stellar Mass
                __galaxy[sector,system,system_meta_data,0,3] = random.uniform(16*__solar_mass,55*__solar_mass)

                # Stellar Luminosity
                # Luminosity = Sun's Luminosity*((Stellar Mass/Sun's Mass)*3.5)
                __galaxy[sector,system,system_meta_data,0,4] = __solar_luminosity * ((__galaxy[sector,system,system_meta_data,0,3]/__solar_mass)*3.5)

                # Stellar Radius
                __galaxy[sector,system,system_meta_data,0,5] = random.uniform(6.6*__solar_radius,100*__solar_radius)

                # Stellar Temperature
                # (Stellar Luminosity / 4*pi*(Stellar Radius ** 2)*Stefan-Boltzmann Constant) ** .25
                __galaxy[sector,system,system_meta_data,0,6] = (__galaxy[sector,system,system_meta_data,0,4] / (4*3.14159*(__galaxy[sector,system,system_meta_data,0,5]**2)*__stefan_boltzmann)) ** .25





            elif __galaxy[sector,system,system_meta_data,0,2] == 2:
                __galaxy[sector,system,system_meta_data,0,3] = random.uniform(2.1*__solar_mass,16*__solar_mass)

                __galaxy[sector,system,system_meta_data,0,4] = __solar_luminosity * ((__galaxy[sector,system,system_meta_data,0,3]/__solar_mass)*3.5)

                __galaxy[sector,system,system_meta_data,0,5] = random.uniform(1.8*__solar_radius,6.6*__solar_radius)

                __galaxy[sector,system,system_meta_data,0,6] = (__galaxy[sector,system,system_meta_data,0,4] / (4*3.14159*(__galaxy[sector,system,system_meta_data,0,5]**2)*__stefan_boltzmann)) ** .25

            elif __galaxy[sector,system,system_meta_data,0,2] == 3:
                __galaxy[sector,system,system_meta_data,0,3] = random.uniform(1.4*__solar_mass,2.1*__solar_mass)

                __galaxy[sector,system,system_meta_data,0,4] = __solar_luminosity * ((__galaxy[sector,system,system_meta_data,0,3]/__solar_mass)*3.5)

                __galaxy[sector,system,system_meta_data,0,5] = random.uniform(1.4*__solar_radius,1.8*__solar_radius)

                __galaxy[sector,system,system_meta_data,0,6] = (__galaxy[sector,system,system_meta_data,0,4] / (4*3.14159*(__galaxy[sector,system,system_meta_data,0,5]**2)*__stefan_boltzmann)) ** .25

            elif __galaxy[sector,system,system_meta_data,0,2] == 4:
                __galaxy[sector,system,system_meta_data,0,3] = random.uniform(1.04*__solar_mass,1.4*__solar_mass)

                __galaxy[sector,system,system_meta_data,0,4] = __solar_luminosity * ((__galaxy[sector,system,system_meta_data,0,3]/__solar_mass)*3.5)

                __galaxy[sector,system,system_meta_data,0,5] = random.uniform(1.15*__solar_radius,1.4*__solar_radius)

                __galaxy[sector,system,system_meta_data,0,6] = (__galaxy[sector,system,system_meta_data,0,4] / (4*3.14159*(__galaxy[sector,system,system_meta_data,0,5]**2)*__stefan_boltzmann)) ** .25

            elif __galaxy[sector,system,system_meta_data,0,2] == 5:
                __galaxy[sector,system,system_meta_data,0,3] = random.uniform(0.8*__solar_mass,1.04*__solar_mass)

                __galaxy[sector,system,system_meta_data,0,4] = __solar_luminosity * ((__galaxy[sector,system,system_meta_data,0,3]/__solar_mass)*3.5)

                __galaxy[sector,system,system_meta_data,0,5] = random.uniform(0.96*__solar_radius,1.15*__solar_radius)

                __galaxy[sector,system,system_meta_data,0,6] = (__galaxy[sector,system,system_meta_data,0,4] / (4*3.14159*(__galaxy[sector,system,system_meta_data,0,5]**2)*__stefan_boltzmann)) ** .25

            elif __galaxy[sector,system,system_meta_data,0,2] == 6:
                __galaxy[sector,system,system_meta_data,0,3] = random.uniform(0.45*__solar_mass,0.8*__solar_mass)

                __galaxy[sector,system,system_meta_data,0,4] = __solar_luminosity * ((__galaxy[sector,system,system_meta_data,0,3]/__solar_mass)*3.5)

                __galaxy[sector,system,system_meta_data,0,5] = random.uniform(0.7*__solar_radius,0.96*__solar_radius)

                __galaxy[sector,system,system_meta_data,0,6] = (__galaxy[sector,system,system_meta_data,0,4] / (4*3.14159*(__galaxy[sector,system,system_meta_data,0,5]**2)*__stefan_boltzmann)) ** .25

            elif __galaxy[sector,system,system_meta_data,0,2] == 7:
                __galaxy[sector,system,system_meta_data,0,3] = random.uniform(0.08*__solar_mass,0.45*__solar_mass)

                __galaxy[sector,system,system_meta_data,0,4] = __solar_luminosity * ((__galaxy[sector,system,system_meta_data,0,3]/__solar_mass)*3.5)

                __galaxy[sector,system,system_meta_data,0,5] = random.uniform(0.08*__solar_radius,0.7*__solar_radius)

                __galaxy[sector,system,system_meta_data,0,6] = (__galaxy[sector,system,system_meta_data,0,4] / (4*3.14159*(__galaxy[sector,system,system_meta_data,0,5]**2)*__stefan_boltzmann)) ** .25

            ### END SYSTEM META DATA ###

            # Set this in order to start populating planet distance.
            __previous_planet_distance = 20000000000

            # For each system, create a random number of planets.
            for planet in range(random.randint(1,max_planets)):


                ### PLANET META DATA ###
                ## 0: Planet ID
                ## 1: Distance from Sun (unit = m)
                ## 2: Planetary Circumference (unit = 1000 miles)
                ## 3: Planetary Mass (unit = 0.1 MicroSuns (Earth is 30))
                ## 4: Orbital Period (unti =  earth day)
                ## 5: Rotation (unit = earth hour)
                ## 6: Planet Type
                ## 7: Planet Effective Temp (unit = kelvin)
                ## 8: Planet Radius (unit = 1 meter)
                ## 9: X Cap
                ## 10: Y Cap
                ## 11: Planetary Bond-Albedo value
                # Set Planet id.
                __galaxy[sector,system,planet,planet_meta_data,0] = __planet_id
                __planet_id += 1

                # Set the max distance.
                __possible_max_distance = __previous_planet_distance * 3

                # Planet's distance from sun, measured in million miles.
                __previous_planet_distance = __galaxy[sector,system,planet,planet_meta_data,1] = random.randint(__previous_planet_distance,__possible_max_distance)

                # Set the Planet's type, first either Gas(1) or Terrestrial(2).
                __galaxy[sector,system,planet,planet_meta_data,6] = random.choice([1,2])
                print(__galaxy[sector,system,planet,planet_meta_data,6])

                # Set Circumference if Gas.
                if __galaxy[sector,system,planet,planet_meta_data,6] == 1:
                    __galaxy[sector,system,planet,planet_meta_data,2] = __circumference = random.randint(max_circumference*3,max_circumference*15)
                    print('Gas')
                # Set Circumference if Terrestrial.
                elif __galaxy[sector,system,planet,planet_meta_data,6] == 2:
                    __galaxy[sector,system,planet,planet_meta_data,2] = __circumference = random.randint(65,max_circumference)
                    print('Terrestrial')

                # Set the planet's mass in 1/100th Earth Mass.
                __galaxy[sector,system,planet,planet_meta_data,3] = random.randint(5,600)

                __radius_in_miles = (100*__galaxy[sector,system,planet,planet_meta_data,2]) / 3.14159 / 2

                # Set the Planet's radius by converting the radius in miles to meters.
                __galaxy[sector,system,planet,planet_meta_data,8] = __radius_in_miles / 0.00062137

                # Set the planet's Bond-Albedo type.
                __galaxy[sector,system,planet,planet_meta_data,11] = random.uniform(0,1)

                # Set the Planet's Effective Temp (in Kelvin)
                # Stellar Temp * ((Stellar Radius / (2 * distance from star)) ** .5) * ((1 - Bond-Albedo) ** .25)
                __galaxy[sector,system,planet,planet_meta_data,7] = __galaxy[sector,system,system_meta_data,0,6] * ((__galaxy[sector,system,system_meta_data,0,5] / (2 * __galaxy[sector,system,planet,planet_meta_data,1])) ** 0.5) * ((1 - __galaxy[sector,system,planet,planet_meta_data,11]) ** 0.25)

                # Convert the planet's effective temp to fahrenheit
                __temp_fahrenheit = kelvin_to_fahrenheit(sector,system,planet)


                print('Stellar type:')
                print(__galaxy[sector,system,system_meta_data,0,2])
                print('Stellar Luminosity')
                print(__galaxy[sector,system,system_meta_data,0,4])
                print('Stellar Radius')
                print(__galaxy[sector,system,system_meta_data,0,5])
                print('Stellar Mass')
                print(__galaxy[sector,system,system_meta_data,0,3])
                print('Stellar Temperature')
                print(__galaxy[sector,system,system_meta_data,0,6])
                print('Distance (million km)')
                print(0.000001*0.001*__galaxy[sector,system,planet,planet_meta_data,1])
                print('Temp kelvin')
                print(__galaxy[sector,system,planet,planet_meta_data,7])
                print('Temp (fahrenheit)')
                print(__temp_fahrenheit)
                print('Planet Type')
                print(__galaxy[sector,system,planet,planet_meta_data,6])
                print('Planet Circumference')
                print(__galaxy[sector,system,planet,planet_meta_data,2])
                print()




                # The Planet's y coor will always be half the x coor.
                __galaxy[sector,system,planet,planet_meta_data,9] = __circumference
                __galaxy[sector,system,planet,planet_meta_data,10] = __circumference // 2

                # Multiplying total x by y gives us the number of regions on the planet.
                __region_count = int(__galaxy[sector,system,planet,planet_meta_data,9] * __galaxy[sector,system,planet,planet_meta_data,10])

                # These increment after each region is created, in order to assign each reason a unique square on the planet's cartesian system.
                __x = 0
                __y = 0

                # Create a shortcut to the current planet's x and y caps.
                __x_cap = __galaxy[sector,system,planet,planet_meta_data,9]
                __y_cap = __galaxy[sector,system,planet,planet_meta_data,10]

                # For each planet, create a number of regions that works with the generated circumference.
                for region in range(__region_count):
                    ### REGION DATA
                    ## 0: Region ID
                    ## 1: Region x Coordinate
                    ## 2: Region y Coordinate
                    ## 3: Region Altitude
                    ## 4: Region Tempurature

                    # Assign the current increment of the region id to this region.
                    __galaxy[sector,system,planet,region,0] = __region_id

                    # Assign the current x and y to this region.
                    __galaxy[sector,system,planet,region,1] = __x
                    __galaxy[sector,system,planet,region,2] = __y

                    ### ONLY FOR TERRESTRIAL PLANETS ###
                    if __galaxy[sector,system,planet,planet_meta_data,6] == 2:
                        ### ALTITUDE GENERATION ###

                        # 0 = West1         1 = West2       2 = South1      3 = South2
                        # 4 = Southwest1    5 = Southwest2  6 = East2       7 = East1
                        # 8 = Southeast1    9 = Southeast2  10 = West by SW
                        # 11=South by SW    12=South by SE  13=East by SE
                        __surrounding_regions = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

                        # West Regions.
                        if __x >= 1:
                            __surrounding_regions[0] = int(region - 1)
                            if __x >= 2:
                                __surrounding_regions[1] = int(region - 2)

                        # South Regions.
                        if __y >= 1:
                            __surrounding_regions[2] = int(region - __x_cap)
                            if __y >= 2:
                                __surrounding_regions[3] = int(region - (__x_cap * 2))

                        # Southwest Regions.
                        if __y >= 1:
                            if __x >= 1:
                                __surrounding_regions[4] = int(region - __x_cap - 1)
                            else:
                                __surrounding_regions[4] = int(region - 1)

                            if __y >= 2:
                                if __x >= 2:
                                    __surrounding_regions[5] = int(region - (__x_cap * 2) - 2)
                                else:
                                    __surrounding_regions[5] = int(region - __x_cap - 2)

                        # East Regions.
                        if (__x + 2) >= __x_cap:
                            __surrounding_regions[6] = int(region - (__x_cap - 2))
                            if (__x + 1) >= __x_cap:
                                __surrounding_regions[7] = int(region - (__x_cap - 1))

                        # Southeast Regions.
                        if __y >= 1:
                            if (__x + 1) >= __x_cap:
                                __surrounding_regions[8] = int(region - ((__x_cap * 2) - 1))
                            else:
                                __surrounding_regions[8] = int(region - (__x_cap - 1))

                            if __y >= 2:
                                if (__x + 2) >= __x_cap:
                                    __surrounding_regions[9] = int(region - ((__x_cap * 3) - 2))
                                else:
                                    __surrounding_regions[9] = int(region - ((__x_cap * 2) - 2))

                        # West by Southwest region.
                        if __y >= 1:
                            if __x >= 2:
                                __surrounding_regions[10] = int(region - (__x_cap + 2))
                            else:
                                __surrounding_regions[10] = int(region - 2)

                        # South by Southwest region.
                        if __y >= 2:
                            if __x >= 1:
                                __surrounding_regions[11] = int(region - ((__x_cap * 2) + 1))
                            else:
                                __surrounding_regions[11] = int(region - (__x_cap + 1))

                        # South by Southeast region.
                        if __y >= 2:
                            if (__x + 1) >= __x_cap:
                                __surrounding_regions[12] = int(region - ((__x_cap * 3) - 1))
                            else:
                                __surrounding_regions[12] = int(region - ((__x_cap * 2) - 1))

                        # East by Southeast region.
                        if __y >= 1:
                            if (__x + 2) >= __x_cap:
                                __surrounding_regions[13] = int(region - ((__x_cap * 2) - 2))
                            else:
                                __surrounding_regions[13] = int(region - (__x_cap - 2))


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
                            __floor = int(__chosen_altitude - __potential_count)
                            __ceiling = int(__chosen_altitude + __potential_count)

                        # The new altitude is somewhere between the lowest and highest possibel.
                        __new_altitude = random.randint(__floor,__ceiling)

                        # Set the Altitude of the new region.
                        __galaxy[sector,system,planet,region,3] = __new_altitude

                        ### END ALTITUDE GENERATION ###



                        ### TEMPERATURE GENERATION ###

                        # Planet Effective Temp.
                        __galaxy[sector,system,planet,planet_meta_data,7]

                        # Region temp is determined by Altitude, Latitude, Greenhouse Effect and Planet Effective Temp.

                        __galaxy[sector,system,planet,region,4] = random.randint(0,7)

                        ### END TEMPERATURE GENERATION ###




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

def kelvin_to_fahrenheit(sector,system,planet):
    return ((__galaxy[sector,system,planet,planet_meta_data,7] - 273.15)*9/5)+32
