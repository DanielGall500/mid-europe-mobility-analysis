from graph import Graph
import plotly.graph_objects as go
import numpy as np 
import sys

class LinePlot(Graph):

	def plot(self, dates, target):
		decrease_target = np.multiply(target,-1)

		line = go.Scatter(x=dates,y=decrease_target)
		return line


