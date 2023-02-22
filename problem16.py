"""
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""

def div(a, b):
	""""
	>>> print(div(4, 5))
	0
	>>> print(div(25, 5))
	5
	"""
	count = 0
	while a >= b:
		a = a - b
		count += 1
	return count
	

if __name__ ==  "__main__":
	import doctest
	doctest.testmod()