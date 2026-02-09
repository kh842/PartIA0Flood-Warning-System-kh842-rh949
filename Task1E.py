from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
   stations= build_station_list()
   print("when N is 9 these are the top 9(or more) rivers "+ str(rivers_by_station_number(stations, 9)))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()