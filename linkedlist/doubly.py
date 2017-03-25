class node (object):
	"""docstring for node """
	def __init__(self):
		self.data=None
		self.next=None
		self.prev=None
		self.head=None
	def setdata(self,data):
		self.data=data
	def getdata(self):
		return self.data
	def setnext(self,next):
		self.next=next
	def getnext(self):
		return self.next
	def setprev(self,prev):
		self.prev=prev
	def getprev(self):
		return self.prev

class doubly(object):
	"""docstring for doubly"""
	def __init__(self,head):
		self.head=head
		self.length=0

	def addbeg(self,data):
		newnode=node()
		newnode.setdata(data)
		newnode.setnext(self.head)
		newnode.setprev(None)
		self.head=newnode
		self.length+=1

	def addend(self,data):
		newnode=node()
		newnode.setdata(data)
		current=self.head
		while (current.getnext()!=None):
			current=current.getnext()
		current.setnext(newnode)
		newnode.setnext(None)
		newnode.setprev(current)
		self.length+=1

	def addpos(self,data,pos):
		newnode=node()
		newnode.setdata(data)
		current=self.head
		for i in range (1,pos):
			current=current.getnext()
		newnode.setprev(current.getprev())
		newnode.setnext(current)
		(current.getprev()).setnext(newnode)
		current.setprev(newnode)
		self.length+=1

	def delbeg(self):
		current=self.head
		self.head=current.getnext()
		self.length-=1

	def delpos(self,pos):
		current=self.head
		for i in range(1,pos):
			current=current.getnext()
		current.getprev().setnext(current.getnext())
		current.getnext().setprev(current.getprev())
		self.length-=1

	def delval(self,value):
		current=self.head
		while(current.getdata()!=value):
			current=current.getnext()
		current.getprev().setnext(current.getnext())
		current.getnext().setprev(current.getprev())
		self.length-=1


	def printlist(self,head):
		temp=self.head
		while(temp!=None):
			print(temp.getdata(),end=" ")
			temp=temp.getnext()
		print()

def main():
	data=[2,5,7,1,4,3]
	head=None
	for i in data:
		newnode=node()
		newnode.setdata(i)
		newnode.setnext(head)
		newnode.setprev(None)
		if(head!=None):
			head.setprev(newnode)
		head=newnode

	list1=doubly(head)
	list1.printlist(head)
	list1.delval(7)
	print ("New List")
	list1.printlist(head)


if __name__ =="__main__":
	main()
	



		