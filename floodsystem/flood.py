#2b
def stations_level_over_threshold(stations, tol):
    """"A function that inputs a list of station objects and a tolerance value, and the outputs a list of tuples,
    where each tuple holds a station object where the relative water level is above the tolerance,
    and the relative water level at each station
    """
    river_tuple=[]

    for i in range(len(stations)):
        new_tuple=(stations[i].name,stations[i].relative_water_level())
        river_tuple.append(new_tuple)
    sorted_river = sorted(river_tuple, key=lambda x: float('-inf') if x[1] is None else x[1], reverse=True)
    filtered = [t for t in sorted_river if t[1] is not None]
    final=[]
    for  i in range(len(filtered)):
     if filtered[i][1]>tol:
         final.append(filtered[i])

    

    return final


#2C

def stations_highest_rel_level(stations, N):
    """A function that inputs a list of station objects and an integer N, and outputs a list
    of objects with the highest relative water level"""

    

    river=[]
    for i in range(len(stations)):
        new_tuple=(stations[i],stations[i].relative_water_level())
        river.append(new_tuple)
    sorted_river = sorted(river, key=lambda x: float('-inf') if x[1] is None else x[1], reverse=True)

    top_N=sorted_river[:N]
    return top_N  