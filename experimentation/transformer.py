from standards import Country, Attribute
import pandas as pd
import sys 

class Transformer:

	def __init__(self):
		return

	#Combines Two Series/Attributes Into One Dataframe
	def _combine(self, A, B, name_A, name_B):
		#Combine Name With Series
		df = { 
		name_A : A, 
		name_B : B
		}

		#Concatenate These Series Into Dataset
		return  pd.concat(df,axis=1)

	#Performs Differencing
	def get_difference(self, y, periods):
		return y.diff(periods=periods)

	#Performs Smoothing
	def get_rolling_mean(self, dates, y, windows):
		#Combine Our Dates & Target Series
		rolling_df = self._combine(dates, y, 'date', 'target')

		#Create Rolling Mean On Target Attribute
		rolling_mean = rolling_df['target'].rolling(
			window=windows).mean()
		return dates, rolling_mean

	#Performs Resampling
	def get_resample(self, dates, y, rule):
		#Combine Our Dates & Target Series
		df = self._combine(dates, y, 'date', 'target')

		#Convert to correct format and set as string
		df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
		df = df.set_index('date')

		#Resample our data
		resample = df.target.resample(rule).mean()
		return resample.index, resample.values
