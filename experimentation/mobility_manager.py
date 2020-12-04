import pandas as pd
from standards import Country, Attribute
import sys

class MobilityManager:

	austria_file = "austria.csv"
	belgium_file = "belgium.csv"
	germany_file = "germany.csv"

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
		return self.get_set(country)[att_str]





















