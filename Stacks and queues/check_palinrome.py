class stack(object):
	def __init__(self):
		self.stk=[]
		self.limit=200
	def push(self,data):
		if len(self.stk)>self.limit:
			print ("Stack Overflow")
		else:
			self.stk.append(data)
	def pop(self):
		if len(self.stk)<=0:
			print ("Stack Underflow")
		else:
			return self.stk.pop()
	def printstack(self):
		print (self.stk)


def check_palendrome(data):
	newstack=stack()
	for i in data:
		newstack.push(i)
	for i in data:
		if i ==newstack.pop():
			continue
		else:
			return False
	return True



data="madam"
print(check_palendrome(data))
