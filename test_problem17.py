import unittest
from problem17 import arithmetic_arranger


class CodeTests(unittest.TestCase):
	def test_too_many_problems(self):
		actual = arithmetic_arranger(["12 + 15", "16 - 7"])
		expected = """  12     16
+ 15   -  7
----   --
		"""
		
		self.assertEqual(actual, None, "This is custom error message")