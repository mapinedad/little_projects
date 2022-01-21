# This Python's document contain a few excercises about asympthotical notation.
# I should be capable of determinate the Big-Oh for many of showed code.
# Give a big-Oh characterization, in terms of n, of the running time of the each example. 

def example_2(S):
	'''Return the sum of the elements with even index in sequence S.'''
	n = len(S)
	total = 0
	for j in range(0, n, 2):
		total += S[j]
	return total

if __name__ == '__main__':

	values_list = [x for x in range(101)]

	even_index_sum = example_2(values_list)

	print(even_index_sum)