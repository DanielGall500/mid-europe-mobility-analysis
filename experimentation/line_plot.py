from graph import Graph
import plotly.graph_objects as go
import numpy as np 
import sys

class LinePlot(Graph):

	def plot(self, dates, target):
		#Represent The Decline In An Attribute
		#target = np.multiply(target,-1)

		#Create Line Plot
		line = go.Scatter(x=dates,y=target)
		return line


