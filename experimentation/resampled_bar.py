import plotly.graph_objects as go
from graph import Graph
import numpy as np

class ResampledBar(Graph):
	def plot(self, country, attribute, rule):
		#Flip The Values
		#target = np.multiply(attribute,-1)

		#Apply Resampling
		dates, target = super().transformer.get_resample(country, 
			attribute, rule)

		#Create The Bar Graph
		bar = go.Bar(x=dates, y=target)
		return bar









