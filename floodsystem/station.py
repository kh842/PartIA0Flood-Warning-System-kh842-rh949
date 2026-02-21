# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

import floodsystem.datafetcher as datafetcher


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
        



    
        
    """def relative_water_level(self):
        This method gives the water level as a number between 0 and compared to the relative range
        latest_level = datafetcher.fetch_latest_water_level_data(self)
        #past_water_level=datafetcher.fetch_measure_levels(self, 100)
        
        #water_level =past_water_level[1]
        low = self.typical_range[0]
        high = self.typical_range[1]
        #high=max(water_level)
        #low=min(water_level)

        #relative= (float(latest_level)-float(low))/(high-low)
        #self.typical_range = typical_range

        #highest typical is 1 lowest is 0, the calc we need to do is current minus lowest water level/divided by range

        return latest_level"""
    
    def relative_water_level(self):

        # Check if typical_range is valid
        if not self.typical_range_consistent():
            return None
        water_levels=datafetcher.fetch_latest_water_level_data()["items"]
        # print(self.latest_level)
        for item in water_levels:
            if item["station"] == self.station_id:
                if "latestReading" not in item.keys():
                    return None
                else:
                    self.latest_level = item["latestReading"]["value"]
        #hi=datafetcher.fetch_latest_water_level_data(self)

        # Extract low/high values
        low = self.typical_range[0]
        high = self.typical_range[1]


        # Calculate relative level
        relative_level = (self.latest_level - low) / (high - low)

        return relative_level
  

     

def stations_level_over_threshold(stations, tol):
    
    river_tuple=[]

    for i in range(len(stations)):
        new_tuple=(stations[i].name,stations[i].relative_water_level())
        river_tuple.append(new_tuple)

    return river_tuple


def inconsistent_typical_range_stations(stations):
    """a function when given a list of station objects, returns a list of stations 
    with inconsistent data"""
    # below uses filter to remove any stations that DO have consistent typical ranges
    station_list = list(filter(lambda x: not x.typical_range_consistent(), stations))
    return station_list

#2C
def stations_highest_rel_level(stations, N):

    list=[]
    for i in range(len(stations)):
        new_tuple=(stations[i].name,stations[i].relative_water_level())
        list.append(new_tuple)
    sorted_list = sorted(list, key=lambda x: x[1], reverse=True)

    top_N=sorted_list[:N]
    return top_N   

