def binary_search_iterative(list1,value):
	low=0
	high=len(list1)-1
	while low<=high:
		mid=low+high//2
		if value>list1[mid]:
			print(list1[mid])
			low=mid
		elif value<list1[mid]:
			high=mid-1
		else:
			return mid
	return -1

list1=[4,6,8,13,21,35,38,67]
print(binary_search_iterative(list1,38))