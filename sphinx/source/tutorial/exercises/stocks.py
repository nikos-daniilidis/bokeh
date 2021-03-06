###
### NOTE: This exercise requires a network connection
###

import numpy as np
import pandas as pd

from bokeh.plotting import figure, output_file, show, VBox

# Here is some code to read in some stock data from the Yahoo Finance API
AAPL = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])
MSFT = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=MSFT&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])
IBM = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=IBM&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])

output_file("stocks.html", title="stocks.py example")

# create a figure
p1 = figure(title="Stocks")

# EXERCISE: finish this line plot, and add more for the other stocks. Each one should
# have a legend, and its own color.
p1.line(
    AAPL['Date'],                                       # x coordinates
    AAPL['Adj Close'],                                  # y coordinates
    color='#A6CEE3',                                    # set a color for the line
    legend='AAPL',                                      # attach a legend label
)

# EXERCISE: style the plot, set a title, lighten the gridlines, etc.

# EXERCISE: start a new figure

# Here is some code to compute the 30-day moving average for AAPL
aapl = AAPL['Adj Close']
aapl_dates = AAPL['Date']

window_size = 30
window = np.ones(window_size)/float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

# EXERCISE: plot a scatter of circles for the individual AAPL prices with legend
# 'close'. Remember to set the x axis type and tools on the first renderer

# EXERCISE: plot a line of the AAPL moving average data with the legeng 'avg'

# EXERCISE: style the plot, set a title, lighten the gridlines, etc.

show(VBox(p1, p2))  # open a browser

