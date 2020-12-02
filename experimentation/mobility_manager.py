import enum

class Country(enum.IntEnum):
	Belgium = 0,
	Germany = 1,
	Austria = 2

class Attribute(enum.IntEnum):
	ID = 0,
	Country = 1,
	Retail_And_Rec = 2,
	Grocery_And_Pharma = 3,
	Parks = 4,
	Transit = 5,
	Workplaces = 6,
	Residential = 7


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

	#Get An Attribute Column For A Country
	def get_attribute(self, country, attribute):
		att_str = self.attributes[str(attribute)]
		return self.country_sets[country][att_str]




