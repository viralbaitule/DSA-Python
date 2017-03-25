def reverse(string):
	end=len(string)-1
	start=0
	while(start<end):
		temp=string[start]
		print(string[end])
		string[start]=string[end]
		string[end]=temp
		start+=1
		end-=1
	return str(string)





string="123456"
print (reverse(list(string)))
