# The plot server must be running
# Go to http://localhost:5006/bokeh to view this plot

import numpy as np
from bokeh.plotting import *
from bokeh.objects import BlazeDataSource
output_server("blazesource")
source = BlazeDataSource(data_url="http://localhost:6030/compute/iris.json",
                         expr={'expr' : 'iris'})

circle('sepal_length', 'sepal_width',
       color='#A6CEE3', tools="pan,wheel_zoom,box_zoom,reset,previewsave",
       source=source)
show()
