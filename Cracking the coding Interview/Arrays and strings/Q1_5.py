def string_conpression(string):
	length=len(string)
	count=1
	check_place=string[0]
	newstring=''
	for i in range(1,length):
		if string[i]==check_place:
			count+=1
		else:
			newstring=newstring+check_place+str(count)
			check_place=string[i]
			count=1
		if i==length-1:
			newstring=newstring+check_place+str(count)
	return newstring



string="aaabbcccdd"
print(string_conpression(string))


