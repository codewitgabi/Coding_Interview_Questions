"""
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
	235
    +  52
       -----
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
output:
	32      3801      45      123
 + 698     -      2   + 43    +  49
     -----        ------       ----       -----
"""

def arithmetic_arranger(problems: list, output: bool = False):
	# write first lines for all problems
	for problem in problems:
		arith_prob = problem.split()
		nums_max_length = max([len(i) for i in arith_prob]) + 2
		
		print(f"{arith_prob[0]:>{nums_max_length}}", end="   ")
	print()
	
	# write second lines for all problems
	for problem in problems:
		arith_prob = problem.split()
		nums_max_length = max([len(i) for i in arith_prob]) + 2
		line_two = arith_prob[1] + " " * (nums_max_length - len(arith_prob[2]) - 1) + arith_prob[2]
		
		print(f"{line_two:>{nums_max_length}}", end="   ")
	print()
	
	# write answer separator for all problems
	for problem in problems:
		arith_prob = problem.split()
		nums_max_length = max([len(i) for i in arith_prob]) + 2
		
		print("-" * nums_max_length, end="   ")
	print()
	
	# write answers for all problems
	if output:
		for problem in problems:
			arith_prob = problem.split()
			answer = eval(f"{arith_prob[0]}{arith_prob[1]}{arith_prob[2]}")
			nums_max_length = max([len(i) for i in arith_prob]) + 2
			
			print(f"{answer:>{nums_max_length}}", end="   ")
		print()
	
	

#arithmetic_arranger(["5632 + 698", "3801 - 2", "45 + 43", "123 + 49", "12 - 17"], True)