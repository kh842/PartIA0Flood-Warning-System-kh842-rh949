from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""
    stations = build_station_list()
    stations_inconsistent_data = inconsistent_typical_range_stations(stations)
    stations_ordered = sorted([station.name for station in stations_inconsistent_data])
    # create station list, find those with inconsistent data, and format + order alphabetically

    print("Stations with inconsistent data:", stations_ordered, sep="\n")


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()