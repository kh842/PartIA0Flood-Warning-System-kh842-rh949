from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number



stations= build_station_list()
stations_list=rivers_with_station(stations)

river_list_norep = []

for river in stations_list:
    if river not in river_list_norep:
        river_list_norep.append(river)

river_list_norep.sort()

#rivers_with_station(stations)

print(str(len(river_list_norep)) + " stations"+ " The first 10 are "+ str(river_list_norep[:9]))


dick= stations_by_river(stations)
test = dick.get("River Aire")
test.sort()
print("The stations in River Aire are "+ str(test))
test = dick.get("River Cam")
test.sort()
print("The stations in River Cam are "+ str(test))
test = dick.get("River Thames")
test.sort()
print("The stations in River Thames are "+ str(test))

hi= len(dick.get("River Thames"))
print(hi)
#print(river_list_norep)
#print(stations_by_river(stations))

print(rivers_by_station_number(stations))
