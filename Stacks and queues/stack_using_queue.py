from queue import *
class stack(object):
	"""docstring for stack"""
	def __init__(self):
		self.que1=Queue()
		self.que2=Queue()

	def push(self,data):
		self.que1.put(data)
		while self.que2.qsize():
			self.que1.put(self.que2.get())
		self.que1, self.que2 =  self.que2, self.que1

	def pop(self):
		top=self.que2.get()
		return top
	def printstack(self):
		for n in range(self.que2.qsize()):
			value=self.que2.get()
			print (value)
			self.que2.put(value)




s=stack()
s.push(6)
s.push(3)
s.push(2)
s.push(7)
s.push(8)

s.printstack()
			