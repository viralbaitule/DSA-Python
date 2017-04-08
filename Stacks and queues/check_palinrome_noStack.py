def check_palendrone(data):
	i=0
	j=len(data)-1
	while i<j:
		if data[i]==data[j]:
			i+=1
			j-=1
		else:
			return False
	return True




data="madam"
print(check_palendrone(data))