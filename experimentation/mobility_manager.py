import enum
import sys
import pandas as pd

class Country(enum.IntEnum):
	Belgium = 0,
	Germany = 1,
	Austria = 2

class Attribute(enum.IntEnum):
	ID = 0,
	Country = 1,
	Date = 2,
	Retail_And_Rec = 3,
	Grocery_And_Pharma = 4,
	Parks = 5,
	Transit = 6,
	Workplaces = 7,
	Residential = 8


class MobilityManager:

	country_sets = {}
	attributes = {}

	def __init__(self, austria_df, belgium_df, germany_df, attributes):
		self.country_sets[Country.Austria] = austria_df
		self.country_sets[Country.Belgium] = belgium_df
		self.country_sets[Country.Germany] = germany_df

		#Save Each Attribute ID => String As Dictionary
		for att_id, att_str in zip(Attribute, attributes):
			self.attributes[str(att_id)] = att_str

	def get_set(self, country):
		return self.country_sets[country]

	#Get An Attribute Column For A Country
	def get_attribute(self, country, attribute):
		att_str = self.attributes[str(attribute)]
		return self.country_sets[country][att_str]

	def get_rolling_mean(self, country, attribute, windows):
		att = self.get_attribute(country, attribute)
		rolling_mean = att.rolling(window=windows).mean()
		return rolling_mean

	def get_resample(self, country, attribute, rule):

		#Get our target resampling attribute and the date index
		att = self.get_attribute(country, attribute)
		index = self.get_attribute(country, Attribute.Date)

		data = {
		"date" : index,
		"target" : att
		}

		#Concatenate these two attributes
		df = pd.concat(data,axis=1)

		#Convert to correct format and set as string
		df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
		df = df.set_index('date')

		#Resample our data
		resample = df.target.resample(rule).mean()
		return resample




















