class Flower(object):
	"""A class that informs about the name, the number of petals and price of flower's"""

	def __init__(self, name, petals, price):
		"""Initialize a Flower instance.

		name	name of the flower.
		petals	flower petals.
		price	flower price (expressed in dollars $)
		"""
		self._name = name
		self._petals = int(petals)
		self._price = float(price)

	def get_name(self):
		"""Return the flower name's"""
		return self._name
	def get_nPetals(self):
		"""Return the number of petals of a given flower."""
		return self._petals
	def get_price(self):
		"""Return the price of a given flower."""
		return self._price
#--------------------------------------MAIN----------------------------

if __name__ == '__main__':

	flower_1 = Flower('Belladona', 10, 14.54)
	flower_2 = Flower('Girasol', 50, 20.38)
	flower_3 = Flower('Rosa', 15, 13.45)

	flower_list = [flower_1, flower_2, flower_3]

	for flower in flower_list:
		print("Flower name: ", flower.get_name())
		print("Numbers of petals:", flower.get_nPetals())
		print("Price:", flower.get_price())
		print()