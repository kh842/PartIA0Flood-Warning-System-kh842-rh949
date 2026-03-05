
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
    print("Aryan is a battyman")
    tuple1=()

    high= stations_level_over_threshold(stations,1.5)
    med= stations_level_over_threshold(stations,1)
    low= stations_level_over_threshold(stations,-100000)
    for i in range (len(high)):
        tuple1.append((str(high[i][0].name) + str(high[i][1])))
    print(tuple1)
    #print(str(high[i][0].name) + str(high[i][1]))
    


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
