import sys
## below path contains the singly and douubly linked list code 
sys.path.insert(0, 'C:/Drive/Study/DSA-Python/custom_modules')
from singly import node,singly

def deletenode(value_node):
	value_node.setdata(value_node.getnext().getdata())
	value_node.setnext(value_node.getnext().getnext())


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
value=6
current=head
while(value!=current.getdata()):
	previous=current
	current=current.getnext()
deletenode(current)
print ("New List")
list1.printlist(head)
