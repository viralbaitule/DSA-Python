def insertion_sort(list1):
	for i in range(1,len(list1)):
		value=list1[i]
		hole=i
		while (hole>0 and value<list1[hole-1]):
			list1[hole]=list1[hole-1]
			hole-=1
		list1[hole]=value


list1=[9,3,5,1,4,2]
insertion_sort(list1)
for i in list1:
	print (i)
