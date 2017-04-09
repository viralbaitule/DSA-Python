import sys
## below path contains the singly and douubly linked list code 
sys.path.insert(0, 'C:/Drive/Study/DSA-Python/custom_modules')
from singly import node,singly

def add(h1,h2):
	num1=0
	carry=0
	l1=h1
	l2=h2
	sum1=[]
	while l1!=None or l2!=None:
		n1=l1.getdata()
		n2=l2.getdata()
		result=int(n1)+int(n2)+carry
		carry=result//10
		result=result%10
		l1=l1.getnext()
		l2=l2.getnext()
		sum1.insert(0,result)
	head3=None
	print (sum1)
	for i in sum1:
		newnode=node()
		newnode.setdata(i)
		newnode.setnext(head3)
		head3=newnode
	




data=[2,5,7]
## linkedlist : 3-> 3-> 1-> 2-> 5->2
head=None
for i in data:
	newnode=node()
	newnode.setdata(i)
	newnode.setnext(head)
	head=newnode

list1=singly(head)
list1.printlist(head)

data2=[1,9,4]
## linkedlist : 3-> 3-> 1-> 2-> 5->2
head2=None
for i in data2:
	newnode2=node()
	newnode2.setdata(i)
	newnode2.setnext(head2)
	head2=newnode2
list2=singly(head2)
list2.printlist(head2)
add(head,head2)