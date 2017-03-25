possibleMcNuggets = [False for i in range(46)]

def McNuggets(n):
	if not isinstance(n, int): return False
	if n < 0: return False
	if n > 45: return True

	if False == possibleMcNuggets[0]:
		possibleMcNuggets[0] = True
		for i in range(46):
			if possibleMcNuggets[i]:
				if i + 6 < 46: possibleMcNuggets[i + 6] = True
				if i + 9 < 46: possibleMcNuggets[i + 9] = True
				if i + 20 < 46: possibleMcNuggets[i + 20] = True

	return possibleMcNuggets[n]

print (McNuggets(33))
