def bubble_sort(list1):
	for i in range (0,len(list1)-1):
		for j in range(0,len(list1)-1):
			if(list1[j]>list1[j+1]):
				list1[j],list1[j+1]=list1[j+1],list1[j]

list1=[9,3,5,1,4,2]
bubble_sort(list1)
for i in list1:
	print (i)
