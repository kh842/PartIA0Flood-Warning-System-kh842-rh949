
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level,stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import matplotlib
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    risk_dict = {}

    #set the different risk levels based on relative water level
    severe_stations = stations_level_over_threshold(stations, 1.5)
    high_stations = stations_level_over_threshold(stations, 1.0)
    low_stations = stations_level_over_threshold(stations, -100000)

    # Add to dictionary. 
    for station_obj, level in severe_stations:
        if station_obj.name not in risk_dict:
            risk_dict[station_obj.name] = "severe"

    for station_obj, level in high_stations:
        if station_obj.name not in risk_dict:
            risk_dict[station_obj.name] = "high"

    for station_obj, level in low_stations:
        if station_obj.name not in risk_dict:
            risk_dict[station_obj.name] = "Low"

    # make tuple
    final_list = list(risk_dict.items())

    # Print every station name that has "severe" as the value
    print("--- Stations with severe Risk ---")
    for name, risk in final_list:
        if risk == "severe":
            print(name)
    


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
