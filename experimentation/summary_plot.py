import plotly.graph_objects as go
from graph import Graph
import numpy as np

class ResampledBar(Graph):

	def plot(self, country, attribute, rule):
		#Retrieve Our Data
		dates, target = super().transformer.get_resample(country, 
			attribute, rule)

		#Make The Values Absolute
		abs_target = np.absolute(target)

		#Create The Bar Chart
		bar = go.Bar(x=dates, y=abs_target)
		return bar









