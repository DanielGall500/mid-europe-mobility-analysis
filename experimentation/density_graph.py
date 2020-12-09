from graph import Graph
import plotly.graph_objects as go
import numpy as np 

class DensityPlot(Graph):

	def plot(self, dates, target, windows):
		#Represent Decline 
		#target = np.multiply(target,-1)

		#Retrieve Rolling Mean
		dates, roll_mean = super().transformer.get_rolling_mean(dates, 
			target, windows)

		#Ensure Density Is Filled In
		fill = 'tozeroy'
		return go.Scatter(x=dates,y=roll_mean, fill=fill)




