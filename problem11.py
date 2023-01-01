"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

def generate_power_set(setObj) -> list:
	output = set()
	output.add(())
	for i in range(len(setObj)):
		output.add((setObj[i],))
		for j in range(i):
			output.add((setObj[i], setObj[j]))
			# as the length of the setObj increase, continue the pattern of the loops
		
	output.add(tuple(setObj))
	return sorted(output, key= len)
	

arr = [1, 2, 3]
print(generate_power_set(arr))