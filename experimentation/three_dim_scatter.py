import plotly.graph_objects as go
from graph import Graph

class CorrScatter(Graph):

	def plot(self, att_A, att_B, att_C):
		scatter = go.Scatter3d(x=att_A,
			y=att_B, z=att_C, mode='markers',name="NAME")

		return scatter

