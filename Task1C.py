from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    CAM_CENTRE = (52.2053, 0.1218)
    # define Cambridge city centre

    stations = build_station_list()
    stations_within_10k = stations_within_radius(stations, CAM_CENTRE, 10)
    stations_ordered = sorted([station.name for station in stations_within_10k])
    # create station list, find those within 10km, and format + order alphabetically

    print("Stations within 10km:", stations_ordered, sep="\n")


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()