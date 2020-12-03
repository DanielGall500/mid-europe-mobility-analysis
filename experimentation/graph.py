import plotly.graph_objects as go
from mobility_manager import MobilityManager

class Graph:

	figure = go.Figure()
	mobility = MobilityManager()

	def __init__(self):
		return

	def _parse_prefs(self, prefs):
		return prefs["title"], prefs["x_title"], prefs["y_title"]

	def add_prefs(self, prefs):
		ttl, x_ttl, y_ttl = self._parse_prefs(prefs)
		self.figure.update_layout(title=ttl, 
			xaxis_title=x_ttl, yaxis_title=y_ttl)
		return self.figure

	def add(self, graph):
		self.figure.add_trace(graph)
		return self.figure

	def show(self):
		self.figure.show()