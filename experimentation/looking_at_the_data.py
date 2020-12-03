import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import mobility_manager as mm
from line_plotter import LinePlot
from density_graph import DensityPlot

mobility_manager = mm.MobilityManager()

dates = mobility_manager.get_attribute(mm.Country.Belgium,
	mm.Attribute.Date)

att = mobility_manager.get_attribute(mm.Country.Belgium, 
	mm.Attribute.Retail_And_Rec)

belgium_preferences = {
	"title" : "Belgium Line Plot",
	"x_title" : "Date",
	"y_title" : "Attribute"
}

plot = DensityPlot()
plot.add_data(mm.Country.Belgium, 
	mm.Attribute.Retail_And_Rec, 10)
plot.add_prefs(belgium_preferences)
plot.show()





























