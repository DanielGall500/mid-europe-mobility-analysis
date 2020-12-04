from transformer import Transformer
from mobility_manager import MobilityManager
from standards import Country, Attribute
from plotly.subplots import make_subplots
from line_plot import LinePlot
from density_graph import DensityPlot
from resampled_bar import ResampledBar
import plotly.graph_objects as go
import sys

class MobilitySuite:

	subplot_rows = None
	subplot_cols = None

	figure = None

	data_manager = MobilityManager()

	def __init__(self, rows, cols):
		self.figure = make_subplots(rows = rows, 
		cols = cols)

		self.subplot_rows = rows
		self.subplot_cols = cols

	def get_plot_line(self, country, attribute):
		#Retrieve Data
		dates = self.data_manager.get_attribute(
			country, Attribute.Date)
		target = self.data_manager.get_attribute(
			country, attribute)

		#Plot Lineplot
		graph_line = LinePlot()
		return graph_line.plot(dates, target)

	def get_plot_density(self, country, attribute, windows):
		#Retrieve Data
		dates = self.data_manager.get_attribute(
			country, Attribute.Date)
		target = self.data_manager.get_attribute(
			country, attribute)

		graph_density = DensityPlot()
		return graph_density.plot(dates, target, windows)

	def get_plot_resampled_bar(self, country, attribute, rule):
		#Retrieve Data
		dates = self.data_manager.get_attribute(
			country, Attribute.Date)

		target = self.data_manager.get_attribute(
			country, attribute)

		graph_resampled_bar = ResampledBar()
		return graph_resampled_bar.plot(dates, target, rule)

	def add_plots(self, plots):
		for i in range(0, self.subplot_rows):
			nxt_plot = plots[i]

			self.figure.add_trace(nxt_plot, 
				row=i+1, col=1)


	def plot(self, country, attribute):
		graph_line = self.get_plot_line(country, attribute)

		num_windows = 20
		graph_density = self.get_plot_density(country, 
			attribute, num_windows)

		rule = 'M'
		graph_bar = self.get_plot_resampled_bar(country,
			attribute, rule)

		self.add_plots([graph_line, graph_density, graph_bar])

	def show(self):
		self.figure.show()






