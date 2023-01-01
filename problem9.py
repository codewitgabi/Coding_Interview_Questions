"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""

class Stack:
	def __init__(self) -> None:
		self._stack = list()
		
	def push(self, value) -> None:
		self._stack.append(value)
		
	def pop(self):
		if not self._stack:
			raise Exception("No item to pop from the list")
		self._stack = self._stack[:-1]
		
	def max(self):
		if not self._stack:
			raise Exception("Can't find max value for empty stack")
		init_max = self._stack[0]
		for item in self._stack:
			if item > init_max:
				init_max = item
		return init_max
		
	def __str__(self):
		return str(self._stack)
		
s = Stack()
s.push(3)
s.push(6)
s.pop()
s.push(4)
print(s.max())
print(s)