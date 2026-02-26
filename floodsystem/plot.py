import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)

    plt.xlabel("Date")
    plt.ylabel("Water level/m")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    new_dates = date2num(dates) - d0
    plt.plot(new_dates, levels)
    plt.plot(new_dates, poly(new_dates))

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()