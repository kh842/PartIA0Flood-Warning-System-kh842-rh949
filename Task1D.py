from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
   """Requirements for Task 1D"""
   
   stations= build_station_list()
   stations_list=rivers_with_station(stations)

   print(str(len(stations_list)) + " stations"+ " The first 10 are "+ str(stations_list[:9]))


   dict= stations_by_river(stations)
   test = dict.get("River Aire")
   test.sort()
   print("The stations in River Aire are "+ str(test))
   test = dict.get("River Cam")
   test.sort()
   print("The stations in River Cam are "+ str(test))
   test = dict.get("River Thames")
   test.sort()
   print("The stations in River Thames are "+ str(test))

   hi= len(dict.get("River Thames"))
   print(hi)
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()