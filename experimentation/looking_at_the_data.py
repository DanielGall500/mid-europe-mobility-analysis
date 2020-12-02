import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import mobility_manager as mm

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

att = mobility_manager.get_attribute(mm.Country.Belgium,
	mm.Attribute.Retail_And_Rec)

print(att)





























