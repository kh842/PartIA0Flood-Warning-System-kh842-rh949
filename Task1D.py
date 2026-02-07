from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river



stations= build_station_list()
stations_list=rivers_with_station(stations)

river_list_norep = []

for river in stations_list:
    if river not in river_list_norep:
        river_list_norep.append(river)

#rivers_with_station(stations)
#print(river_list_norep)
print(stations_by_river(stations))
