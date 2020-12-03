from line_plotter import LinePlot
import plotly.graph_objects as go
from transformer import Transformer
from mobility_manager import MobilityManager


class DensityPlot(LinePlot):

	def add_data(self, country, attribute, windows):
		manager = super().mobility

		#Retrieve Rolling Mean
		dates, roll_mean = manager.get_rolling_mean(country, 
			attribute, windows)

		#Ensure Density Is Filled In
		line = go.Scatter(x=dates,y=roll_mean, fill='tozeroy')

		#Call Back To Inherited Class
		super().fig.add_trace(line)
		return super().fig



