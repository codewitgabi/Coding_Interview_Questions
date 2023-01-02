def longest_palindromic_string(char: str) -> str:
	substrings = []
	str_length = len(char)
	for i in range(str_length):
		for j in range(i, str_length):
			substring = char[j: str_length]
			if substring == substring[::-1]:
				substrings.append(substring)				
	substrings.sort()
	return substrings[-1]
	

print(longest_palindromic_string("banana"))
print(longest_palindromic_string("aabcdcb"))
