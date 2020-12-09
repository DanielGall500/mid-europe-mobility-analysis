from mobility_manager import MobilityManager
from standards import Country, Attribute
from plotly.subplots import make_subplots
from line_plot import LinePlot
from density_graph import DensityPlot
from resampled_bar import ResampledBar
import plotly.graph_objects as go
import numpy as np 
import sys

class MobilitySuite:

	#Number Of Rows/Cols Of Subplots
	subplot_rows = None
	subplot_cols = None

	figure = None

	#Mobility Manager Created
	data_manager = MobilityManager()

	def __init__(self, rows, cols):
		#Create Subplots
		self.figure = make_subplots(rows = rows, 
		cols = cols)

		self.subplot_rows = rows
		self.subplot_cols = cols


	def plot_corr(self, country, att_one, att_two):
		series_one = self.data_manager.get_attribute(
			country, att_one)

		series_two = self.data_manager.get_attribute(
			country, att_two)

		corr = np.corrcoef(x=series_one,y=series_two)
		print(corr)

		scatter = go.Scatter(x=series_one,y=series_two,
			mode='markers')

		self.add_plots([scatter])

	"""
	This plotting function below is the powerhouse of our 
	suite. It combines everything we have worked on thus
	far into one function.
	"""
	def plot(self, country, attribute, density_windows,
		resampling_bar_rule):
		#Retrieve Our Data
		dates = self.data_manager.get_attribute(
			country, Attribute.Date)
		target = self.data_manager.get_attribute(
			country, attribute)

		#Create A Line Graph
		graph_line = self.get_plot_line(dates, target)

		#Create A Density Graph
		graph_density = self.get_plot_density(dates, 
			target, density_windows)

		#Create A Bar Graph
		graph_bar = self.get_plot_resampled_bar(dates,
			target, resampling_bar_rule)

		#Add These Plots As Subplots
		self.add_plots([graph_line, graph_density, graph_bar])

	def get_plot_line(self, dates, target):
		#Lineplot Class 
		graph_line = LinePlot()
		return graph_line.plot(dates, target)

	def get_plot_density(self, dates, target, windows):
		#Density Plot Class
		graph_density = DensityPlot()
		return graph_density.plot(dates, target, windows)

	def get_plot_resampled_bar(self, dates, target, rule):
		#Resampled Bar Class
		graph_resampled_bar = ResampledBar()
		return graph_resampled_bar.plot(dates, target, rule)

	#Add A List Of Subplots
	def add_plots(self, plots):
		for i in range(0, self.subplot_rows):
			nxt_plot = plots[i]

			self.figure.add_trace(nxt_plot, 
				row=i+1, col=1)

	#Show The Graph
	def show(self):
		self.figure.show()






