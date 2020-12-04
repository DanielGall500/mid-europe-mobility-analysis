from graph import Graph
import plotly.graph_objects as go
import numpy as np 

class DensityPlot(Graph):

	def plot(self, dates, target, windows):
		transformer = super().transformer

		#Retrieve Rolling Mean
		dates, roll_mean = transformer.get_rolling_mean(dates, 
			target, windows)

		decrease_roll_mean = np.multiply(roll_mean,-1)

		#Ensure Density Is Filled In
		fill = 'tozeroy'
		return go.Scatter(x=dates,y=decrease_roll_mean, fill=fill)




