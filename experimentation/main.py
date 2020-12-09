from suite import MobilitySuite
from standards import Country,Attribute

def main():
	suite = MobilitySuite(1,1)

	suite.plot_corr(Country.Austria, Attribute.Retail_And_Rec, 
		Attribute.Grocery_And_Pharma)

	suite.show()

if __name__ == "__main__":
	main()
