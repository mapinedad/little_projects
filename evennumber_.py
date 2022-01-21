"""Excercise 2°: Write a short Python function, is_even(k),
that takes an integer value and returns True if k is even, and False
otherwise. However, your function cannot use multiplicacion,
modulo, or division operatos."""

def is_even(k):
	q = 0
	r = k

	while r >= 2:
		r = r - 2
		q += 1 
	return (True if (r == 0) else False)
#----------------------------------------------------
print("""Welcome, please enter an integer: """)

integer = int(input(" "))
result_bool = is_even(integer)

if result_bool == True:
	print("Even.")
else:
	print("Not Even.")