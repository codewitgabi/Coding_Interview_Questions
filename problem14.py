"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

"""

from itertools import zip_longest

def edit_distance(str1: str, str2: str) -> int:
	"""
	>>> print(edit_distance("kitten", "sitting"))
	3
	>>> print(edit_distance("sittings", "sitting"))
	1
	>> print(edit_distance("sitting", "sitting"))
	0
	"""
	distance = 0
	for data in zip_longest(str1, str2):
		char1, char2 = data
		if char1 != char2:
			distance += 1
	
	return distance
		

if __name__ == "__main__":
	import doctest
	doctest.testmod()