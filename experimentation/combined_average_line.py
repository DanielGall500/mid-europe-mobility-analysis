from graph import Graph
import plotly.graph_objects as go

class CombinedAveragePlot(Graph):

	def plot(self, dates, cA_data, cB_data, cC_data, name):

		avg_series = (cA_data + cB_data + cC_data) / 3.0

		#Retrieve Rolling Mean
		dates, roll_mean = super().transformer.get_rolling_mean(dates, 
			avg_series, 20)

		combined_avg = go.Scatter(x=dates, 
			y=roll_mean,
			name=name)

		return combined_avg
