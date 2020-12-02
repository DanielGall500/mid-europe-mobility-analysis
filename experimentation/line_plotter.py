import plotly.graph_objects as go 

class LinePlot:

	fig = go.Figure()

	def __init__(self):
		return None

	def create(self, x, y):
		line = go.Scatter(x=x,y=y)

		self.fig.add_trace(line)

		return self.fig


