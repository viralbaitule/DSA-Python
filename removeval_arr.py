def removeval_arry(nums,val):
	i=j=0
	while j< len(nums):
		if nums[j]==val:
			j+=1
		else:
			nums[i]=nums[j]
			i+=1
			j+=1
	return nums[:i]

nums=[1,2,4,6,2,7,9,2,1]
val=2
print(removeval_arry(nums,val))