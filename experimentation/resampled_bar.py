import plotly.graph_objects as go
from graph import Graph
import numpy as np

class ResampledBar(Graph):

	def plot(self, country, attribute, rule):
		#Retrieve Our Data
		dates, target = super().transformer.get_resample(country, 
			attribute, rule)

		#Make The Values Absolute
		decrease_target = np.multiply(target,-1)

		#Create The Bar Chart
		bar = go.Bar(x=dates, y=decrease_target)
		return bar









