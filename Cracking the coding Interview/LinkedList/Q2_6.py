import sys
## below path contains the singly and douubly linked list code 
sys.path.insert(0, 'C:/Drive/Study/DSA-Python/custom_modules')
from singly import node,singly
class stack(object):
	def __init__(self):
		self.stk=[]
		self.limit=200
	def push(self,data):
		if len(self.stk)>self.limit:
			print ("Stack Overflow")
		else:
			self.stk.append(data)
	def pop(self):
		if len(self.stk)<=0:
			print ("Stack Underflow")
		else:
			return self.stk.pop()
	def printstack(self):
		print (self.stk)


def check_palandrome(head):
	mystack=stack()
	slow=fast=head
	while fast and fast.getnext():
		mystack.push(slow.getdata())
		slow=slow.getnext()
		fast=(fast.getnext()).getnext()
	
	if fast:
		slow=slow.getnext()
	while slow:
		if mystack.pop()!=slow.getdata():
			return False
		else:
			slow=slow.getnext()
	return True





string="madam"
head=None
for i in string:
	newnode=node()
	newnode.setdata(i)
	newnode.setnext(head)
	head=newnode

list1=singly(head)
list1.printlist(head)
print(check_palandrome(head))

