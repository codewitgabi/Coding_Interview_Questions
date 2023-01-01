def auto_complete(s:str, query:list) -> list:
	"""
	>>> auto_complete("de", ["dog", "deer", "deal"])
	['deer', 'deal']
	>>> auto_complete("dea", ["dog", "deer", "deal"])
	['deal']
	>>> auto_complete("dears", ["dog", "deer", "deal"])
	[]
	"""
	
	for index, char in enumerate(s):
		for data in query:
			if data[index] == s[index]:
				break
			else:
				query.remove(data)
	return query
	
	
if __name__ == "__main__":
	import doctest
	doctest.testmod()