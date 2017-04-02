
def merge_sort(list1):
	if len(list1)>1:
		mid=len(list1)//2
		lefthalf=list1[:mid]
		righthalf=list1[mid:]
		merge_sort(lefthalf)
		merge_sort(righthalf)
		i=j=k=0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]<righthalf[j]:
				list1[k]=lefthalf[i]
				i+=1
			else:
				list1[k]=righthalf[j]
				j+=1
			k+=1
		while i<len(lefthalf):
			list1[k]=lefthalf[i]
			i+=1
			k+=1
		while j<len(righthalf):
			list1[k]=righthalf[j]
			j+=1
			k+=1





list1=[9,3,5,1,4,2]
merge_sort(list1)
print (list1)