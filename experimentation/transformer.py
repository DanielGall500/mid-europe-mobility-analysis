import pandas as pd

class Transformer:

	def __init__(self):
		return

	def get_rolling_mean(self, dates, y, windows):
		#Combine Two Attributes
		df = {
		'date' : dates,
		'target' : y
		}
		rolling_df = pd.concat(df,axis=1)

		#Create Rolling Mean On Target Attribute
		rolling_mean = rolling_df['target'].rolling(
			window=windows).mean()
		return dates, rolling_mean

	def get_resample(self, dates, y, rule):
		data = {
		"date" : dates,
		"target" : y
		}

		#Concatenate these two attributes
		df = pd.concat(data, axis=1)

		#Convert to correct format and set as string
		df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
		df = df.set_index('date')

		#Resample our data
		resample = df.target.resample(rule).mean()
		return resample
