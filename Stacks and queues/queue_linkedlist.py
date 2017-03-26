class node (object):
	"""docstring for node """
	def __init__(self):
		self.data=None
		self.next=None
	def setdata(self,data):
		self.data=data
	def getdata(self):
		return self.data
	def setnext(self,next):
		self.next=next
	def getnext(self):
		return self.next

class queue(object):
	"""docstring for queue"""
	def __init__(self, limit=10):
		self.limit = limit
		self.start=None
		self.end=None
		self.head=None
	def enqueue(self,data):
		newnode=node()
		newnode.setdata(data)
		if self.head==None:
			newnode.setnext(None)
			self.head=newnode
			self.start=newnode
		else:
			self.end.setnext(newnode)
		self.end=newnode
	def dequeue(self):
		temp=self.head.getdata()
		self.head=self.head.getnext()
		return temp
	def printqueue(self):
		temp=self.head
		while temp!=None:
			print (temp.getdata())
			temp=temp.getnext()

q=queue()
q.enqueue(3)
q.enqueue(9)
q.enqueue(6)
q.enqueue(8)
q.printqueue()
print ("dequeue")
print(q.dequeue())


		
		