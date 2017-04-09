import sys
## below path contains the singly and douubly linked list code 
sys.path.insert(0, 'C:/Drive/Study/DSA-Python/custom_modules')
from singly import node,singly


def intersection(head1,head2):
	l1=0
	l2=0
	list1=head1
	list2=head2
	while list1:
		l1+=1
		list1=list1.getnext()
	while list2:
		l2+=1
		list2=list2.getnext()
	if l1>l2:
		larger=l1
		smaller=l2
	else:
		larger=l2
		smaller=l1

	diff=larger-smaller
	list1=head1
	list2=head2
	if l1>l2:
		for i in range(diff):
			list1=list1.getnext()
	else:
		for i in range(diff):
			list2=list2.getnext()

	while list1.getdata()!=list2.getdata():
		list1=list1.getnext()
		list2=list2.getnext()

	return list1.getdata()

	






data=[90,45,12,2,5,7,6,1,8]
## linkedlist : 3-> 3-> 1-> 2-> 5->2
head=None
for i in data:
	newnode=node()
	newnode.setdata(i)
	newnode.setnext(head)
	head=newnode

list1=singly(head)
list1.printlist(head)

data2=[90,45,12,10,9,4]
## linkedlist : 3-> 3-> 1-> 2-> 5->2
head2=None
for i in data2:
	newnode2=node()
	newnode2.setdata(i)
	newnode2.setnext(head2)
	head2=newnode2
list2=singly(head2)
list2.printlist(head2)
print(intersection(head,head2))