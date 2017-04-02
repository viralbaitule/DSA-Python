def quick_sort(list1,start,end):
	if start<end:
		pindex=partition(list1,start,end)
		quick_sort(list1,start,pindex-1)
		quick_sort(list1,pindex+1,end)

def partition(list1,start,end):
	pivot=list1[end]
	pindex=start
	for i in range(start,end):
		if list1[i]<=pivot:
			list1[i],list1[pindex]=list1[pindex],list1[i]
			pindex+=1
	list1[pindex],list1[end]=list1[end],list1[pindex]
	return pindex




list1=[9,3,5,1,4,2]
quick_sort(list1,0,len(list1)-1)
print (list1)