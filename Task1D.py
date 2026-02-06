from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station


stations= build_station_list()
stations_list=rivers_with_station(stations)

stations_list_norep = []

for river in stations_list:
    if river not in stations_list_norep:
        stations_list_norep.append(river)

#rivers_with_station(stations)
print(stations_list_norep)