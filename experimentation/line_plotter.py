import plotly.graph_objects as go 

class LinePlot:

	fig = go.Figure()

	def __init__(self):
		return None

	def _parse_prefs(self, prefs):
		return prefs["title"], prefs["x_title"], prefs["y_title"]

	def add_prefs(self, prefs):
		ttl, x_ttl, y_ttl = self._parse_prefs(prefs)
		self.fig.update_layout(title=ttl, 
			xaxis_title=x_ttl, yaxis_title=y_ttl)
		return self.fig

	def add_data(self, x, y):
		line = go.Scatter(x=x,y=y)
		self.fig.add_trace(line)
		return self.fig

	def show(self):
		self.fig.show()


