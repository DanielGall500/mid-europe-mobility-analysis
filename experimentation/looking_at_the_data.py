import numpy as np
import pandas as pd
import plotly.express as px

austria_file = "austria.csv"
germany_file = "germany.csv"
belgium_file = "belgium.csv"

def get_dataset(f):
	return pd.read_csv("./datasets/{}".format(f))

ds_austria = get_dataset(austria_file)
ds_germany = get_dataset(germany_file)
ds_belgium = get_dataset(belgium_file)

print(ds_belgium.head())
print(ds_austria.head())
print(ds_germany.head())