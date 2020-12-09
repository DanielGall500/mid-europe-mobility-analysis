import pandas as pd
from standards import Country, Attribute

class MobilityManager:

	#Our CSV Files
	austria_file = "austria.csv"
	belgium_file = "belgium.csv"
	germany_file = "germany.csv"

	"""
	In order to be able to use the standardised 
	attribute enum we created, we will need a dictionary to 
	convert from these attribute enums to the column 
	name thatwe need from the dataframe.

	For our Countries, we'll store each dataframe itself 
	inside the dict as this is simpler.

	TLDR:
	Dicts Convert 
	(Attribute Enum) => (Column String)
	(Country Enum) => (Country DataFrame)
	"""
	attribute_converter = {}
	country_converter = {}

	def __init__(self):
		#Load Our Dataset From CSV File
		austria_set = self._load_dataset(self.austria_file)
		belgium_set = self._load_dataset(self.belgium_file)
		germany_set = self._load_dataset(self.germany_file)

		#Store Our Dataset In Dict
		self.country_converter[Country.Austria] = austria_set
		self.country_converter[Country.Belgium] = belgium_set
		self.country_converter[Country.Germany] = germany_set

		#Store Our Attributes in Dict
		attributes = austria_set.columns
		for att_id, att_str in zip(Attribute, attributes):
			self.attribute_converter[str(att_id)] = att_str

	#Load In A Dataset From CSV File
	def _load_dataset(self, f):
		return pd.read_csv("./datasets/{}".format(f))

	#Get A Saved Dataset
	def get_set(self, country):
		return self.country_converter[country]

	#Get Attribute Data For A Particular Country
	def get_attribute(self, country, attribute):
		att_str = self.attribute_converter[str(attribute)]
		return self.get_set(country)[att_str]





















