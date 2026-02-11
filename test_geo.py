"""Unit test for the geo module"""

from floodsystem.geo import *
from floodsystem.stationdata import build_stations_list

def test_stations_by_distance():
    # build station list
    station_list = build_stations_list()
    centre = (52.2053, 0.1218)
    stations_ordered = stations_by_distance(station_list, centre)
    previous_value = 0
    for station in stations_ordered:
        assert(type(station) == tuple) # check each item is a tuple
        assert(station[1] >= previous_value) # ensures the list is ordered by distance
        previous_value = station[1]

def test_stations_within_radius():
    # build station list
    station_list = build_stations_list()
    centre = (52.2053, 0.1218)
    distance_max = 150
    stations_in_radius = stations_within_radius(station_list, centre, distance_max)
    for station in stations_in_radius:
        distance = haversine(centre, station.coord)
        assert(distance <= distance_max)