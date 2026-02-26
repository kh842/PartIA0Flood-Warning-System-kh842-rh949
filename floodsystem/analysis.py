import matplotlib as mpl
import numpy as np

def polyfit(dates, levels, p):
    converted_dates = mpl.dates.date2num(dates)
    d0 = converted_dates[0]
    p_coeff = np.polyfit(converted_dates - d0, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0


