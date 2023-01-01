import time

"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

def job_scheduler(f, n: int):
	time.sleep(n/1000)
	f()
	

def foo():
	print("Jello world")

job_scheduler(foo, 4000)