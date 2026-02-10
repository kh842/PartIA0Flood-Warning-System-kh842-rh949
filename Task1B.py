from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""
    CAM_CENTRE = (52.2053, 0.1218)
    # define Cambridge city centre

    stations = build_station_list()
    stations_ordered = stations_by_distance(stations, CAM_CENTRE)
    stations_formatted = [(station[0].name, station[0].town, station[1]) for station in stations_ordered]
    # create station list, order them by distance, and create a list with the appropriate tuples

    print("Closest 10 stations:", stations_formatted[:10], sep="\n")
    print("\n\n")
    print("Furthest 10 stations:", stations_formatted[-10:], sep="\n")

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
