def binary_search_recersive(list1,value,low=0,high=-1):
	if not list1: return -1
	if(high == -1): 
		high = len(list1) - 1

	if low==high:
		if list1[low]==value:
			return low
		else:
			return -1
			
	mid=(low+ high)//2

	if list1[mid]>value:
		high=mid-1
		return binary_search_recersive(list1,value,low,high)
	elif list1[mid]<value:
		low=mid+1
		return binary_search_recersive(list1,value,low,high)
	else:
		return mid
	


list1=[3,5,7,9,13,16,19]
loc=binary_search_recersive(list1,16)
print(loc)