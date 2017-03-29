
class queue(object):
	"""docstring for queue"""
	def __init__(self,limit=10):
		self.stack1 =[]
		self.stack2 =[]
		self.limit=limit
		
	def enqueue(self,data):
		for i in self.stack1:
			self.stack2.append(i)
		self.stack1.append(data)
		for i in self.stack2:
			self.stack1.append(i)

	def dequeue(self):
		return self.stack1.pop()

q=queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(8)
print(q.dequeue())
print(q.dequeue())

		