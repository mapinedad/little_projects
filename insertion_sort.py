'''Insertion Sort Algorithm'''

def insertion_sort(S):

	for j in range(1, len(S), 1):

		val = S[j] 
		
		# insert S[j] into the sorted sequence S[1..j-1]
		
		i = j-1

		while i >= 0 and S[i] > val: 

			S[i+1] = S[i]
			
			i -= 1

		S[i+1] = val

	return S


if __name__ == '__main__':

	sequence = [190.0923, 29283, 929, 31, 41, 59, 26, 41, 58]
	sequence_sorted = insertion_sort(sequence)

	print(sequence_sorted)
