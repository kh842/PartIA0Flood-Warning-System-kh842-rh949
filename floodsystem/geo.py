# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    station_list = []
    for station in stations:
        distance = haversine(p, station.coord)
        station_list.append(station, distance)
    return sorted_by_key(station,1)

def stations_within_radius(stations, centre, r):
    stations_with_distance = stations_by_distance(stations, centre)
    station_list = []
    for station in stations_with_distance:
        if station[1] <= r:
            station_list.append(station[0])
    return station_list
