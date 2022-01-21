class Vector():
	"""Represent a vector in a multidimensional space."""

	def __init__(self, n):
		"""Create n-dimensional vector of zeros."""
		self._coords = [0]*n

	def __len__(self):
		"""Return the dimension of the vector."""
		return len(self._coords)

	def __getitem__(self, k):
		"""Return kth coordinate of vector."""
		return self._coords[k]

	def __setitem__(self, k, val):
		"""Set kth coordinate of vector to given value."""
		self._coords[k] = val

	def __add__(self, other):
		"""Return sum of two vectors."""
		if len(self) != len(other): # relies on __len__ method.
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for i in range(len(self)):
			result[i] = self[i] + other[i]
		return result

	def __sub__(self, other):
		"""Return the difference of two vectors."""
		if len(self) != len(other): # relies on __len__ method.
			raise ValueError('dimensions must agree')
		difference = Vector(len(self))
		for i in range(len(self)):
			difference[i] = self[i] - other[i]
		return difference
	
	def __mul__(self, val):
		"""Return new vector with coordinates that are val time the respective coordinates of a original vector."""
		if not isinstance(val, (int, float)):
			raise ValueError('multiplicative factor must be numeric')
		newVector = Vector(len(self))
		for i in range(len(self)):
			newVector[i] = self[i] * val
		return newVector

	def __neg__(self):
		"""Return a new vector in which all coordinates are negative."""
		self._negCoords = Vector(len(self._coords))
		for i in range(len(self._coords)):
			self._negCoords[i] = -(self._coords[i])
		return self._negCoords

	def __eq__(self, other):
		"""Return True if vector has same coordinates as other."""
		return self._coords == other._coords

	def __ne__(self, other):
		"""Return True if vector differs from other."""
		return not self == other # rely on existing __eq__ definition.
		
	def __str__(self):
		"""Produce string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>' #adapt list representation.

#--------------------------------------------MAIN----------------------------------------------------------------------

if __name__ == '__main__':
	v = Vector(5) # Construct five-dimensional <0, 0, 0, 0, 0> (v and m)
	m = Vector(5) # Construct five-dimensional <0, 18, 0, 0, 55>
	w = Vector(5)
	v[1] = 23 # <0, 23, 0, 0, 0> (based on use of __setitem__)
	v[-1] = 45 # <0, 23, 0, 0, 45> (also via __setitem__)
	m[1] = 18
	m[-1] = 55
	w = -v
	lista = list((1, 2, 3, 5, 6))
	print(w)
	vector = w * 3
	print(vector)
	#suma = m + lista		 # good
	#suma_inverse = lista + m # wrong
	#print(suma) # vector suma printed as <1, 20, 3, 5, 61>
	#print(suma_inverse) # TypeError: can only concatenate list (not "Vector") to list
	"""print(v[4]) # print 45 (via __getitem__)
	u = v + v  # <0, 46, 0, 0 90> (via __add__)
	n = v - m
	print(u)    # print <0, 46, 0, 0, 90>
	print("\n", n)
	print("Vector with all coordinates turn to negative values: ", w)
	total = 0
	for entry in v: # implicit iteration via __len__ and __getitem__
		#print(entry)
		total += entry
	print(total)	"""