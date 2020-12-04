import enum

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