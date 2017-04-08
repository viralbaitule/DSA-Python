class stack(object):
	"""docstring for stack"""
	def __init__(self):
		self.stk = []

	def push(self,data):
		self.stk.append(data)
	def pop (self):
		return self.stk.pop(data)
	def peek (self):
		return self.stk[-1]
	def isempty(self):
		return len(stk)==0

def infix_to_postfix(data):
	newstack=stack()


string="A+B+C*D"
infix_to_postfix(string)
		