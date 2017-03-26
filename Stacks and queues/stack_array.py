
class stack(object):
	"""docstring for stack"""
	def __init__(self, limit=10):
		self.top=None
		self.data=None
		self.stk=[]
		self.limit=limit

	def push (self,data):
		if len(self.stk)>=self.limit:
			print ("Stack Overflow")
			return 0
		self.stk.append(data)
	def pop (self):
		if len(self.stk)<=0:
			print("Stack Underflow")
			return 0
		return self.stk.pop()
	def peek(self):
		return self.stk[-1]
	def isEmpty(self):
		return len(self.stk)==0
	def isFull(self):
		return len(self.stk)==limit
	def printstack(self):
		print (self.stk)

s=stack()
s.push(5)
s.push(4)
s.push(6)
s.printstack()
s.pop()
s.printstack()



		
		
		