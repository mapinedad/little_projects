"""﻿
	The p-norm of a vector v = (v1, v2, . . . , vn) in n-dimensional space is defined as ∥v∥ = sqrt(v1^p + v2^p + · · · + vn^p.)^1/p
	For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector. 
	For example, the Euclidean norm of a √o-dimensi√al vector√ith coordinates (4, 3) has a Euclidean norm of sqrt(4^2 + 3^2) = sqrt(16 + 9) = sqrt(25) = 5. 
	Give an implementation of a function named norm such that norm(v, p) 
	returns the p-norm value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.
"""

from math import sqrt, pow

def norm(v, p=2):
	p_norm = 0.0
	sum_value = 0.0
	for i in v:
		sum_value += pow(i, p)
	p_norm = pow(sum_value, (1/p))
	return p_norm


if __name__ == '__main__':

	prompt = input("Enter an arbitrary numbers, separated by space. This program calculate de p-norm value of a vector: ")
	vector = list(prompt.split())
	p = len(vector)

	for i in range(len(vector)):
		vector[i] = float(vector[i])

	print(norm(vector, p))