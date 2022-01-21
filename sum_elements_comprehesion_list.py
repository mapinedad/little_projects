"""
	Built-in sum function be combined with Python’s
	comprehension syntax to compute the sum of all numbers in an n×n data
	set, represented as a list of lists.
"""


def sum_elements(data_set: list) -> float:

	return sum(map(sum, data_set))

def sum_elements_comprehesion(data_ = list) -> float:

	pass


if __name__ == '__main__':
	
	data = [[1, 2, 3], [4, -5, 8], [9, 2, 3], [5, 3, 2], [90, -46, 53]]
	print(sum_elements(data))
