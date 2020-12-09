from multiline_plot import MultilinePlot
from standards import Country, Attribute
from mobility_manager import MobilityManager
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from combined_average_line import CombinedAveragePlot
from three_dim_scatter import CorrScatter

class CentralEuropeSuite:

	#Number Of Rows/Cols Of Subplots
	subplot_rows = None
	subplot_cols = None

	figure = None
	prefs = None

	"""
	refs = {
	"scatter_title" : "SCATTER",
	"scatter_x_ttl" : "DATES",
	"scatter_y_ttl" : "PERCENT",
	"scatter_trace_A" : "BELGIUM",
	"scatter_trace_B" : "GERMANY",
	"scatter_trace_C" : "AUSTRIA",
	"corr_title" : "CORR",
	"corr_x_ttl" : "XX",
	"corr_y_ttl" : "YY",
	"cor_z_ttl" : "ZZ"
	}
	"""

	#Mobility Manager Created
	data_manager = MobilityManager()

	def __init__(self, rows, cols, height, width, prefs):
		self.prefs = prefs

		scatter_ttl = self.prefs["scatter_ttl"]
		average_ttl = self.prefs["average_ttl"]

		#Create Subplots
		self.figure = make_subplots(rows = rows, 
		cols = cols, subplot_titles=[scatter_ttl, average_ttl])

		self.figure.update_layout(height=height, width=width)

		self.subplot_rows = rows
		self.subplot_cols = cols

	def plot(self, attribute, country_A, country_B, country_C):
		#Retrieve Our Data
		dates = self.data_manager.get_attribute(
			country_A, Attribute.Date)

		cA_data = self.data_manager.get_attribute(
			country_A, attribute)
		cB_data = self.data_manager.get_attribute(
			country_B, attribute)
		cC_data = self.data_manager.get_attribute(
			country_C, attribute)

		scatter_A_ttl = self.prefs["scatter_trace_A"]
		scatter_B_ttl = self.prefs["scatter_trace_B"]
		scatter_C_ttl = self.prefs["scatter_trace_C"]


		scatter_A, scatter_B, scatter_C = self.get_multiline_plot(
			dates, cA_data, cB_data, cC_data,
			scatter_A_ttl, scatter_B_ttl, scatter_C_ttl)

		x_scatter_t = self.prefs["scatter_x_ttl"]
		y_scatter_t = self.prefs["scatter_y_ttl"]

		ttl_avg = self.prefs["average_ttl"]
		x_avg_t = self.prefs["average_x_axis"]
		y_avg_t = self.prefs["average_y_axis"]

		self.add_traces([scatter_A, scatter_B, scatter_C],1,1,
			 x_avg_t, y_avg_t)

		combined_avg_plot = self.get_combined_average_plot(dates, 
			cA_data, cB_data, cC_data, ttl_avg)
		self.add_traces([combined_avg_plot], 2,1,
			 x_avg_t, y_avg_t)

	def get_combined_average_plot(self, dates, country_A, country_B, country_C, name):
		avg_plot = CombinedAveragePlot()
		return avg_plot.plot(dates, country_A, country_B, country_C, name)


	def get_multiline_plot(self, dates, country_A, country_B, country_C,
		name_A, name_B, name_C):
		ml_plot = MultilinePlot()
		plot = ml_plot.plot(dates, country_A, country_B, country_C,
			name_A, name_B, name_C)
		return plot 

	def get_corr_scatter(self, attribute, 
		country_A, country_B, country_C):

		corr_fig = go.Figure()

		#Retrieve Our Data
		dates = self.data_manager.get_attribute(
			country_A, Attribute.Date)

		cA_data = self.data_manager.get_attribute(
			country_A, attribute)
		cB_data = self.data_manager.get_attribute(
			country_B, attribute)
		cC_data = self.data_manager.get_attribute(
			country_C, attribute)

		ttl = self.prefs["corr_title"]
		x_ttl = self.prefs["corr_x_ttl"]
		y_ttl = self.prefs["corr_y_ttl"]
		z_ttl = self.prefs["corr_z_ttl"]

		plotter = CorrScatter()
		corr_scat = plotter.plot(
			cA_data, cB_data, cC_data)

		corr_fig.add_trace(corr_scat)

		corr_fig.update_layout(scene = dict(
		    xaxis_title=x_ttl,
		    yaxis_title=y_ttl,
		    zaxis_title=z_ttl,
		))

		corr_fig.update_layout(title=ttl)

		return corr_fig

	def add_traces(self, traces, row, col, x_ttl, y_ttl):
		for trace in traces:
			self.figure.add_trace(trace,
				row=row, col=col)

			self.figure.update_xaxes(
				title_text=x_ttl, row=row, col=1)

			self.figure.update_yaxes(
				title_text=y_ttl, row=row, col=1)

	#Show The Graph
	def show(self):
		self.figure.show()

def main():

	prefs = {
	"scatter_ttl" : "Belgium, Austria & Germany",
	"scatter_x_ttl" : "Dates",
	"scatter_y_ttl" : "Change (%)",
	"scatter_trace_A" : "Belgium",
	"scatter_trace_B" : "Germany",
	"scatter_trace_C" : "Austria",
	"average_ttl" : "Average Of Three Countries (Rolling Mean)",
	"average_x_axis" : "Dates",
	"average_y_axis" : "Change (%)",
	"corr_title" : "Correlation Between Countries",
	"corr_x_ttl" : "Belgium",
	"corr_y_ttl" : "Germany",
	"corr_z_ttl" : "Austria"
	}


	ce_suite = CentralEuropeSuite(3,1, 1000, 1000, prefs)
	ce_suite.plot(Attribute.Retail_And_Rec, Country.Belgium,
		Country.Germany, Country.Austria)

	corr_scatt = ce_suite.get_corr_scatter(Attribute.Retail_And_Rec, Country.Belgium,
		Country.Germany, Country.Austria)
	corr_scatt.show()

	ce_suite.show()

if __name__ == "__main__":
	main()

