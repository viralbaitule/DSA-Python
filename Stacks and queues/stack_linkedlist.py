class node():
	"""docstring for node"""
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
	def isempty(self):
		return self.head==None
	def hasnext(self):
		return self.next!=None

class stack(object):
	"""docstring for stack"""
	def __init__(self,limit=10):
		self.data=None
		self.head=None
		self.limit=limit
		self.length=0
	def push(self,data):
		newnode=node()
		newnode.setdata(data)
		newnode.setnext(self.head)
		self.head=newnode
		self.length+=1
	def pop(self):
		temp=self.head.getdata()
		self.head=self.head.getnext()
		self.length-=1
		return temp
	def peek(self):
		return self.head.getdata()
	def isEmpty(self):
		return self.head==None
	def isFull(self):
		return self.length>=limit
	def printstack(self):
		temp=self.head
		while temp!=None:
			print (temp.getdata())
			temp=temp.getnext()


s=stack()
s.push(5)
s.push(3)
s.push(2)
s.printstack()
print("top of stack")
print(s.peek())
print(s.isEmpty())
