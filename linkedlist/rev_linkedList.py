class node:
	def __init__(self,data):
		self.data=data
		self.next=None

def reverese(head):
	rev=None
	curr=head
	while curr:
		rev, rev.next, curr = curr, rev, curr.next
	return rev


def main():
	data=[2,5,7,1,4,3]
	head=None
	for i in data:
		newnode=node(i)
		newnode.data=i
		newnode.next=head
		head=newnode
	head=reverese(head)
	temp=head
	while(temp!=None):
		print(temp.data,end=" ")
		temp=temp.next

main()