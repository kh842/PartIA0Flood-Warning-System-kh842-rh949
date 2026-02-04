# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from math import cos, acos, pi

def cos_deg(degrees):
    return cos(degrees/360 * 2 * pi)


def haversine(c1, c2):
    hav_theta = (1-cos_deg(c1[0]-c2[0]))/2 + cos_deg(c1[0])* cos_deg(c2[0]) * (1-cos_deg(c1[1]-c2[1]))/2
    theta = acos(1-2*hav_theta)
    # above we use the appropriate formula to calculate the central angle between the two points
    return 6371 * theta
    # we multiply by the radius to obtain the distance


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
