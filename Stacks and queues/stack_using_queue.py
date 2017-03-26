from queue import *
class stack(object):
	"""docstring for stack"""
	def __init__(self):
		self.que1=Queue()
		self.que2=Queue()

	def push(self,data):
		self.que1.put(data)
		while self.que1.qsize()>1:
			self.que2.put(self.que1.get())
		self.que1, self.que2 =  self.que2, self.que1

	def pop(self):
		top=self.que2.get()
		return top
	def printstack(self):
		for n in range(self.que2.qsize()):
			print (self.que2[n])




s=stack()
s.push(6)
s.printstack()
			