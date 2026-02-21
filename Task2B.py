from floodsystem.stationdata import build_station_list
from floodsystem.station import stations_level_over_threshold


stations = build_station_list()



hi= stations_level_over_threshold(stations,0)
print(hi)