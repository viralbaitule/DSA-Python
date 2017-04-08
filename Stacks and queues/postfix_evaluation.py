class stack(object):
	def __init__(self):
		self.stk=[]
	def push(self,data):
		self.stk.append(data)
	def pop (self):
		return self.stk.pop()
	def peek(self):
		return self.stk[-1]
	def isempty(self):
		return len(self.stk)==0

def postfix_evaluation(data):
	operand_stack=stack()
	data=data.split()
	for i in data:
		if i in "1234567890":
			operand_stack.push(int(i))
		else:
			op1=operand_stack.pop()
			op2=operand_stack.pop()
			result=calculate(i,op1,op2)
			operand_stack.push(result)
	return operand_stack.pop()


def calculate(operator,op1,op2):
	if operator=="+":
		return int(op1)+int(op2)
	elif operator=="-":
		return op2-op1
	elif operator=="*":
		return op1*op2
	elif operator=="/":
		return op2/op1

print(postfix_evaluation('1 2 3 * + 5 - '))
