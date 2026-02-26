from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
import datetime

def run():
    stations = build_station_list()
    top_stations = stations_highest_rel_level(stations, 5)
    for station in top_stations:
        station = station[0]
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=2))
        plot_water_level_with_fit(station, dates, levels, 4)

run()