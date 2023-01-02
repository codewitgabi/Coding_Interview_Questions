"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out: 2, 1.5, 2, 3.5, 2, 2, 2
"""

def running_median(arr: list) -> None:
	for i in range(len(arr)):
		sorted_arr = sorted(arr[: i + 1])
		if len(sorted_arr) % 2 == 1:
			median = sorted_arr[len(sorted_arr) // 2]
		else:
			median = (sorted_arr[len(sorted_arr) // 2 - 1] + sorted_arr[len(sorted_arr) // 2]) / 2
		print(median)
		
		
running_median([2, 1, 5, 7, 2, 0, 5])