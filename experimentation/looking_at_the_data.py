import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import mobility_manager as mm
from line_plotter import LinePlot

def get_dataset(f):
	return pd.read_csv("./datasets/{}".format(f))

austria_file = "austria.csv"
belgium_file = "belgium.csv"
germany_file = "germany.csv"

austria_set = get_dataset(austria_file)
belgium_set = get_dataset(belgium_file)
germany_set = get_dataset(germany_file)

mobility_manager = mm.MobilityManager(austria_set, 
	belgium_set, germany_set, austria_set.columns)


dates = mobility_manager.get_attribute(mm.Country.Belgium,
	mm.Attribute.Date)

retail = mobility_manager.get_attribute(mm.Country.Belgium,
	mm.Attribute.Retail_And_Rec)

plot = LinePlot().create(dates, retail)
plot.show()





























