"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""

def first_missing_positive_integer(arr:list) -> int:
	arr = sorted(list(filter(lambda x: x > 0, arr)))
	for i in range(len(arr) - 1):
		if arr[i] + 1 != arr[i+1]:
			return arr[i] + 1
	return arr[-1] + 1


print(first_missing_positive_integer([3, 4, -1, 1]))
print(first_missing_positive_integer([1, 2, 0]))
