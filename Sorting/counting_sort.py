def counting_sort(l1):
	count=[0 for x in range(10)]
	bucket=[0 for x in range(len(l1))]
	for i in l1:
		count[i]+=1
	for i in range(1,len(count)):
		count[i]+=count[i-1]
	for i in l1:
		bucket[count[i]-1]=i
		count[i]-=1
	return bucket

l1=[3,5,3,1,9,4,2,2,1,6]
bucket=counting_sort(l1)
print (bucket)