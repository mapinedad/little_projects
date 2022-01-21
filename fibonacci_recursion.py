def fibonacci(n):
	"""
		Return pair of Fibonacci numbers, F(n) and F(n-1).
	"""

	if n <= 1:
		return (n, 0)
	else:
		(a, b) = fibonacci(n-1)
		print(a, b)
		return (a+b, a)

if __name__ == '__main__':
	import sys

	sys.setrecursionlimit(1000000) # change the default limit of recursion to 1000000

	result = fibonacci(1000)
	print(result)