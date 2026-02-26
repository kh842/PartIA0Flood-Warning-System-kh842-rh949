# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

import floodsystem.datafetcher as datafetcher
#from floodsystem.stationdata import update_water_levels


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """method that checks range of data for consistency, retursn true if data is consistent 
        and false if data is false"""
        if not self.typical_range:
            return False
            # returns false for any stations with no data
        elif self.typical_range[0] > self.typical_range[1]:
            return False
            # returns false for any stations with typical low below typical high
        else:
            return True
        



    #2b    
    def relative_water_level(self):
        if self.latest_level is None:
            return None
        if not self.typical_range_consistent():
            return None

        low, high = self.typical_range

        if high - low == 0:
            return None

        return (self.latest_level - low) / (high - low)
  

     

def stations_level_over_threshold(stations, tol):
    
    river_tuple=[]

    for i in range(len(stations)):
        new_tuple=(stations[i].name,stations[i].relative_water_level())
        river_tuple.append(new_tuple)
    sorted_river = sorted(river_tuple, key=lambda x: float('-inf') if x[1] is None else x[1], reverse=True)
    filtered = [t for t in sorted_river if t[1] is not None]
    final=[]
    for  i in range(len(filtered)):
     if filtered[i][1]>tol:
         final.append(filtered[i])

    

    return final


def inconsistent_typical_range_stations(stations):
    """a function when given a list of station objects, returns a list of stations 
    with inconsistent data"""
    # below uses filter to remove any stations that DO have consistent typical ranges
    station_list = list(filter(lambda x: not x.typical_range_consistent(), stations))
    return station_list
 

