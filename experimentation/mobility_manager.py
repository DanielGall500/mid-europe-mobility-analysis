import enum
import pandas as pd
from transformer import Transformer

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

	austria_file = "austria.csv"
	belgium_file = "belgium.csv"
	germany_file = "germany.csv"

	transformer = Transformer()

	country_sets = {}
	attributes = {}

	def __init__(self):
		austria_set = self._load_dataset(self.austria_file)
		belgium_set = self._load_dataset(self.belgium_file)
		germany_set = self._load_dataset(self.germany_file)

		self.country_sets[Country.Austria] = austria_set
		self.country_sets[Country.Belgium] = belgium_set
		self.country_sets[Country.Germany] = germany_set

		#Save Each Attribute ID => String As Dictionary
		attributes = austria_set.columns
		for att_id, att_str in zip(Attribute, attributes):
			self.attributes[str(att_id)] = att_str

	def _load_dataset(self, f):
		return pd.read_csv("./datasets/{}".format(f))

	def get_set(self, country):
		return self.country_sets[country]

	#Get An Attribute Column For A Country
	def get_attribute(self, country, attribute):
		att_str = self.attributes[str(attribute)]
		return self.country_sets[country][att_str]

	def get_rolling_mean(self, country, attribute, windows):
		dates = self.get_attribute(country,Attribute.Date)
		y = self.get_attribute(country, attribute)

		return self.transformer.get_rolling_mean(dates, y, windows)

	def get_resample(self, country, attribute, rule):
		#Get our target resampling attribute and the date index
		dates = self.get_attribute(country, Attribute.Date)
		y = self.get_attribute(country, attribute)

		return self.transformer.get_resample(dates, y, rule)

	def get_difference(self, country, attribute, periods):
		return self.transformer.get_difference(y, periods)





















