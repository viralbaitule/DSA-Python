class stack(object):
	"""docstring for stack"""
	def __init__(self):
		self.stk = []

	def push(self,data):
		self.stk.append(data)
	def pop (self):
		return self.stk.pop()
	def peek (self):
		return self.stk[-1]
	def isempty(self):
		return len(self.stk)==0

def infix_to_postfix(data):
	operator_stack=stack()
	prec={}
	prec["/"]=3
	prec["*"]=3
	prec["+"]=2
	prec["-"]=2
	prec["("]=1
	oprand_list=[]
	for i in data:
		if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in "1234567890":
			oprand_list.append(i)
		elif i is "(":
			operator_stack.push(i)
		elif i is ")":
			top=operator_stack.pop()
			while top!="(":
				oprand_list.append(top)
				top=operator_stack.pop()
		else:
			while (not operator_stack.isempty()) and prec[operator_stack.peek()]>=prec[i]:
				oprand_list.append(operator_stack.pop())
			operator_stack.push(i)

	while not operator_stack.isempty():
		oprand_list.append(operator_stack.pop())
	return oprand_list




string="A+B+C*D"
print(infix_to_postfix(string))
		