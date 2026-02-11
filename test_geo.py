"""Unit test for the geo module"""

from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    # build station list
    station_list = build_station_list()
    centre = (52.2053, 0.1218)
    stations_ordered = stations_by_distance(station_list, centre)
    previous_value = 0
    for station in stations_ordered:
        assert(type(station) == tuple) # check each item is a tuple
        assert(station[1] >= previous_value) # ensures the list is ordered by distance
        previous_value = station[1]

def test_stations_within_radius():
    # build station list
    station_list = build_station_list()
    centre = (52.2053, 0.1218)
    distance_max = 150
    stations_in_radius = stations_within_radius(station_list, centre, distance_max)
    for station in stations_in_radius:
        distance = haversine(centre, station.coord) # calculate distance from the centre
        assert(distance <= distance_max) # check all stations are within specified distance

def test_rivers_with_station():
    # build station list
    station_list = build_station_list()
    rivers =  rivers_with_station(station_list)
    for river in rivers:
        assert(rivers.count(river) == 1) # check each item only appears once

def test_stations_by_river():
    # build station list
    station_list = build_station_list()
    rivers_and_stations = stations_by_river(station_list)
    for river in rivers_and_stations:
        for station in rivers_and_stations[river]:
            assert(river == station.river) # check each key maps to the correct station

def test_rivers_by_station_number():
    # build station list
    station_list = build_station_list()
    rivers = rivers_by_station_number(station_list, 3)

    # check the rivers dict is in order
    assert(rivers[0][1] >= rivers[1][1])
    assert(rivers[1][1] >= rivers[2][1])

    # check the station counts match up
    stations_count = [0,0,0]
    for station in station_list:
        if station.river == rivers[0][0]:
            stations_count[0] += 1
        elif station.river == rivers[1][0]:
            stations_count[1] += 1
        elif station.river == rivers[2][0]:
            stations_count[2] += 1

    assert(rivers[0][1] == stations_count[0])
    assert(rivers[1][1] == stations_count[1])
    assert(rivers[2][1] == stations_count[2])
        

test_rivers_by_station_number()
test_rivers_with_station()
test_stations_by_river() 
