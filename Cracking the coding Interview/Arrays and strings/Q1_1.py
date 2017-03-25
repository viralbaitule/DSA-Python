def isunique(string_test):
	boolarray=[False for x in range(256)]
	for i in range(0,len(string_test)):

		if (boolarray[ord(string_test[i])]==True):
			return False
		else:
			boolarray[ord(string_test[i])]=True
	return True		


string="sajbocv"
print (isunique(string))
