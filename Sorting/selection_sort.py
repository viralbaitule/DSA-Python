def selection_sort(list1):
	for i in range(0,len(list1)):
		min_var=i
		for j in range(i+1,len(list1)):
			if (list1[j]<list1[min_var]):
				min_var=j
		list1[i],list1[min_var]=list1[min_var],list1[i]




list1=[6,3,8,1,2,4]
selection_sort(list1)
for i in list1:
	print (i)