class node:
	def __init__(self):
		self.data=None
		self.next=None
		self.head=None
	def setdata(self,data):
		self.data=data
	def getdata(self):
		return self.data
	def setnext(self,next):
		self.next=next
	def getnext(self):
		return self.next	
	def isEmpty(self):
		return self.head==None
	def hasnext(self):
		return self.next!=None

class singly(object):
	"""constructor for singly class"""
	def __init__(self,head):
		self.head = head
		self.length=0

	def addbeg(self,data):
		newnode=node()
		newnode.setdata(data)
		newnode.setnext(self.head)
		self.head=newnode
		self.length+=1

	def addend(self,data):
		newnode=node()
		newnode.setdata(data)
		newnode.setnext(None)
		temp=self.head
		while (temp.getnext()!=None):
			temp=temp.getnext()
		temp.setnext(newnode)
		self.length+=1

	def addpos(self,pos,data):
		newnode=node()
		newnode.setdata(data)
		temp=self.head
		if pos==1:
			addbeg(data)
		for i in range(1,pos-1):
			temp=temp.getnext()
		newnode.setnext(temp.getnext())
		temp.setnext(newnode)
		self.length+=1
		
	def delbeg(self):
		temp=self.head
		self.head=temp.getnext()
		self.length-=1

	def delpos(self,pos):
		current=self.head
		previous=None
		if pos==1:
			delbeg()
		for i in range(1,pos):
			previous=current
			current=current.getnext()
		previous.setnext(current.getnext())
		self.length-=1

	def delvalue(self,value):
		previous=None
		current=self.head
		while(value!=current.getdata()):
			previous=current
			current=current.getnext()
		previous.setnext(current.getnext())
		self.length-=1

	def reverse(self):
		current=self.head
		previous=None
		while current!=None:
			nex=current.getnext()
			current.setnext(previous)
			previous=current
			current=nex
		self.head=previous

	def printlist(self,head):
		temp=self.head
		while(temp!=None):
			print(temp.getdata(),end=" ")
			temp=temp.getnext()
		print()
