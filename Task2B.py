from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    hi= stations_level_over_threshold(stations,0.8)
    for i in range(len(hi)):
        print(str(hi[i][0])+"  "+str(hi[i][1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
