import sys
## below path contains the singly and douubly linked list code 
sys.path.insert(0, 'C:/Drive/Study/DSA-Python/custom_modules')
from singly import node,singly

def kth_to_last(pos,head):
	current=head
	fast=head
	for i in range(pos):
		fast=fast.getnext()
	while(fast!=None):
		fast=fast.getnext()
		current=current.getnext()
	return current.getdata()

data=[2,5,6,1,4,3]
## linkedlist : 3-> 3-> 1-> 2-> 5->2
head=None
for i in data:
	newnode=node()
	newnode.setdata(i)
	newnode.setnext(head)
	head=newnode

list1=singly(head)
list1.printlist(head)
pos=3
current=head

'''
while(value!=current.getdata()):
	previous=current
	current=current.getnext()
'''
print ("Value at kth from last")
print(kth_to_last(pos,head))
