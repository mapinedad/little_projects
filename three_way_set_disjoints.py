'''Three-Way Set Disjointness: 
Suppose there are three sequences of numbers, and on each sequence A, B and C which not contains duplicate values, but that there may
be some numbers that are in two or three of the sequences.

The real problem is determine if the intersection of the three sequences is empty.'''

from time import time, time_ns
from random import randint

def disjoint_1(A, B, C):	# the running time and space of this algorithm is O(n^3) [big-O notation notation for worst case running time]

	'''Return True if there is no element common to all three lists.'''

	for a in A:
		for b in B:
			for c in C:
				if a == b == c:
					return False	# we found a common value
	return True	# if we reach this, sets are disjoint

def disjoint_2(A, B, C):	# the running time and space of this algorithm is O(n^2) [big-O notation for worst case running time]
	
	'''Return True if there is no element common to all three lists.'''

	for a in A:
		for b in B:
			if a == b:	# only check C if we found match from A and B
				for c in C:
					if a == c:	# (and this a == b == c)
						return False	# we found a common value
	return True	# if we reach this, sets are disjoint

if __name__ == '__main__':

	A_set = {x for x in range(randint(1, 10**2009234), 3)}
	B_set = {x for x in range(randint(20, 14**20000), 2)}
	C_set = {x for x in range(randint(0, 8 ** 120000000), 1)}
	
	#print(A_set, B_set, C_set)
	
	time_1 = time_ns()

	result_1 = disjoint_1(A_set, B_set, C_set)
	
	time_2 = time_ns()

	result_2 = disjoint_2(A_set, B_set, C_set)

	time_3 = time_ns()

	print(f"First function: {result_1} -> running time: {time_2 - time_1}")
	print(f"Second function: {result_2} -> running time: {time_3 - time_2}")