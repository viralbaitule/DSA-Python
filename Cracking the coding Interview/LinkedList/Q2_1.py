import sys
## below path contains the singly and douubly linked list code 
sys.path.insert(0, 'C:/Drive/Study/DSA-Python/custom_modules')
from singly import node,singly

def remove_duplicates_hashtable(head):
	current=head
	unique_check={}
	count=0
	previous=None
	while current!=None:
		if current.getdata() not in unique_check.keys():
			unique_check[current.getdata()]=True
			previous=current
		else:
			previous.setnext(current.getnext())
		current=current.getnext()

def remove_duplicates_normal(head):
	current=head
	while current!=None:
		fast=current
		while fast.getnext()!=None:
			if current.getdata()==fast.getnext().getdata():
				fastnext=fast.getnext()
				fast.setnext(fastnext.getnext())
			else:
				fast=fast.getnext()
		current=current.getnext()


data=[2,5,2,1,3,3]
## linkedlist : 3-> 3-> 1-> 2-> 5->2
head=None
for i in data:
	newnode=node()
	newnode.setdata(i)
	newnode.setnext(head)
	head=newnode

list1=singly(head)
list1.printlist(head)

remove_duplicates_normal(head)
print ("New List")
list1.printlist(head)