# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from math import cos, acos, pi

def cos_deg(degrees):
    """This function takes an input in degrees and returns the cosine of the input"""
    return cos(degrees/360 * 2 * pi)


def haversine(c1, c2):
    hav_theta = (1-cos_deg(c1[0]-c2[0]))/2 + cos_deg(c1[0])* cos_deg(c2[0]) * (1-cos_deg(c1[1]-c2[1]))/2
    theta = acos(1-2*hav_theta)
    # above we use the appropriate formula to calculate the central angle between the two points
    return 6371 * theta
    # we multiply by the radius to obtain the distance

#task 1b
def stations_by_distance(stations, p):
    station_list = []
    for station in stations:
        # iterates through station list, calculating the distance and adding the appropriat tuple
        distance = haversine(p, station.coord)
        station_list.append((station, distance))
    return sorted_by_key(station_list,1)

def stations_within_radius(stations, centre, r):
    # uses stations by distance to find station distances from the centre
    stations_with_distance = stations_by_distance(stations, centre)
    station_list = []
    for station in stations_with_distance:
        # only adds stations within distance r to final station list
        if station[1] <= r:
            station_list.append(station[0])
    return station_list


#task 1d
def rivers_with_station(stations):
    stations_list=[]

    for i in range (len(stations)):
        stations_list.append(stations[i].river)
    return stations_list



def stations_by_river(s_list):

    river_dict = {}

    #for i in range (len(r_list)):

        #river_dict[r_list[i]]=  None

    
    for s in s_list:
        if s.river not in river_dict:
            river_dict[s.river] = []

        river_dict[s.river].append(s.name)

    river_list_norep = []

    for river in river_dict:
        if river not in river_list_norep:
            river_list_norep.append(river)

    river_list_norep.sort()

    return river_dict

    
    
#task 1e
def rivers_by_station_number(s_list, N):

    """This function takes an input of a list of station objects and an arbitary number,
       the function counts up how many monitering stations are along each river and puts them into a tuple
       and then orders them from highest to lowest number of stations and outputs the top N rivers along
       with the number of stations they have, if there is a tie it extends the number of rivers of the output 
       until there is no tie.
    """


    dick= stations_by_river(s_list) #creates a dictionary of all the river and their stations
    dick_counter  = {} #create sempty dictionary to count how many stations along each river

    for s in s_list:
        if s.river not in dick_counter:
            dick_counter[s.river]=[] #adds each river to dick_counter
        
            dick_counter[s.river] = len(dick.get(s.river)) #adds how many stations there are to the dictionary

    sorted_dick= dict(sorted(dick_counter.items(), key=lambda item: item[1], reverse=True)) #sorting the dictionary into highest to lowest order
    dick_tuple = tuple(sorted_dick.items()) #makes dict into tuple to manipualte

          
    cut_off= dick_tuple[N-1][1] #finds cut off number of stations incase there is a tie
    for i in range (len(dick_tuple)): #finds which river to end at
        if dick_tuple[i-1][1] == cut_off:
            n=i
    return dick_tuple[:n] #outputs the top N rivers along with number of stations







