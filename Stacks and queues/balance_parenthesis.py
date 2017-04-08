class stack(object):
	"""docstring for stack"""
	def __init__(self):
		self.stk=[]
		self.limit=100
	def push(self,data):
		if len(self.stk)<self.limit:
			self.stk.append(data)
		else:
			print("Stack Overflow")
	def pop(self):
		if len(self.stk)<=0:
			print("Stack Underflow")
		else:
			return self.stk.pop()
	def peek(self):
		return self.stk[-1]
	def stacklength(self):
		return len(self.stk)
	def printstack(self):
		print (self.stk)
#		for i in self.stk:
#			print (i)


def checkparenthesis(data):
	newstack=stack()
	for i in data:
		if i in "[{(":
			newstack.push(i)
		if i in "}])":
			if newstack.peek()==None:
				return False
			stacktop=newstack.pop()
			
			if not ispair(stacktop,i):
				return False
	if newstack.stacklength()>=1:
		return False
	else:
		return True
def ispair(a,b):
	if a=="(" and b==")" or a=="{" and b=="}" or a=="[" and b=="]":
		return True

tem="[(12)]{1}{[(32)22(33)44]52(21)1111}"
print(checkparenthesis(tem))

		