from suite import MobilitySuite
from standards import Country,Attribute

def main():
	suite = MobilitySuite(3,1)

	suite.plot(Country.Austria, Attribute.Transit)

	suite.show()

if __name__ == "__main__":
	main()
