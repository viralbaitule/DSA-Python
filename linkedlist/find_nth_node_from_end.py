from singly import node,singly

def find_nth_from_last(head,n):
	current=head
	fast=head
	for i in range(0,n):
		fast=fast.getnext()
	while fast.getnext()!=None:
		current=current.getnext()
		fast=fast.getnext()
	return current.getdata()
	



data=[2,5,7,1,4,3,9,11,12]
head=None
for i in data:
	newnode=node()
	newnode.setdata(i)
	newnode.setnext(head)
	head=newnode

mylist=singly(head)
mylist.printlist(head)
print(find_nth_from_last(head,0))
