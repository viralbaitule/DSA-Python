from queue import *
class stack(object):
	"""docstring for stack"""
	def __init__(self):
		self.que=Queue()

	def push(self,data):
		self.que.put(data)
		for i in range(self.que.qsize()-1):
			self.que.put(self.que.get())

	def pop(self):
		top=self.que.get()
		return top
	def printstack(self):
		for n in range(self.que.qsize()):
			value=self.que.get()
			print (value)
			self.que.put(value)




s=stack()
s.push(6)
s.push(3)
s.push(2)
s.push(7)
s.push(8)
s.pop()
s.printstack()
