import plotly.graph_objects as go
from graph import Graph


class MultilinePlot(Graph):

	def plot(self, dates, country_A, country_B, country_C,
		name_A, name_B, name_C):

		scatter_A = go.Scatter(x=dates, y=country_A, 
			mode='markers', name=name_A)

		scatter_B = go.Scatter(x=dates,y=country_B,
			mode='markers', name=name_B)

		scatter_C = go.Scatter(x=dates,y=country_C,
			mode='markers', name=name_C)

		return scatter_A, scatter_B, scatter_C
