from graph import Graph
import plotly.graph_objects as go

class LinePlot(Graph):

	def add_data(self, x, y):
		line = go.Scatter(x=x,y=y)
		super().figure.add_trace(line)
		return super().figure


