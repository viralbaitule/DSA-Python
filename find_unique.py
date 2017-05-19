

def unique(list1):
	length=len(list1)
	old=list1[0]
	pos=1
	for i in range (1,length):
		new =list1[i]
		if (new!=old):
			list1[pos]=new
			pos+=1
		old=new
	return pos




list1=[5,3,3,1,1,6,6,6,8,9,3,2,1,5]
print(unique(list1))
