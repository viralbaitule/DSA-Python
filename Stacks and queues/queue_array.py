class queue(object):
	"""docstring for queue"""
	def __init__(self, limit=10):
		self.limit=limit
		self.que = []

	def enqueue(self,data):
		self.que.insert(0,data)

	def dequeue(self):
		self.que.pop()

	def isEmpty(self):
		return len(self.que)==0

	def isFull(self):
		return len(self.que)>=self.limit
		
	def printqueue(self):
		print(self.que)


q=queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(8)
q.printqueue()
q.dequeue()
q.dequeue()
q.printqueue()