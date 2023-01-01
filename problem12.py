"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def segregate_array(arr: list) -> list:
	for i in range(len(arr) - 1, 0, -1):
		for j in range(i):
			if arr[j] < arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr
	
	
print(segregate_array(['G', 'B', 'R', 'R', 'B', 'R', 'G']))