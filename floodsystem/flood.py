#2C
def stations_highest_rel_level(stations, N):

    river=[]
    for i in range(len(stations)):
        new_tuple=(stations[i],stations[i].relative_water_level())
        river.append(new_tuple)
    sorted_river = sorted(river, key=lambda x: float('-inf') if x[1] is None else x[1], reverse=True)

    top_N=sorted_river[:N]
    return top_N  