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

	subplot_rows = 4
	subplot_cols = 1

	figure = None

	data_manager = MobilityManager()

	def __init__(self):
		self.figure = make_subplots(rows = self.subplot_rows, 
		cols = self.subplot_cols)

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

	def plot(self, country, attribute):
		graph_line = self.get_plot_line(country, attribute)
		self.figure.add_trace(graph_line,row=1,col=1)

		num_windows = 20
		graph_density = self.get_plot_density(country, 
			attribute, num_windows)
		self.figure.add_trace(graph_density, row=2, col=1)

		rule = 'M'
		graph_bar = self.get_plot_resampled_bar(country,
			attribute, rule)
		self.figure.add_trace(graph_bar, row=3, col=1)

		self.figure.show()


def main():
	suite = MobilitySuite()
	suite.plot(Country.Germany, Attribute.Retail_And_Rec)

if __name__ == "__main__":
	main()




