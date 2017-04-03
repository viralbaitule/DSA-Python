class binaryTreeNode(object):
	"""docstring for binaryTreeNode"""
	def __init__(root, data):
		root.data = data
		root.right=None
		root.left=None


def insert(root,node):
	if root==None:
		root=node
	else:
		if root.data>node.data:
			if root.left == None:
				root.left = node
			else:
				insert(root.left,node)
		else:
			if root.right==None:
				root.right=node
			else:
				insert(root.right,node)

def searchNode(root,value):
	if root==None:
		return False
	else:
		if root.data==value:
			return True
		if root.data<value:
			return searchNode(root.right,value)
		else:
			return searchNode(root.left,value)
	return False


root=binaryTreeNode(4)
insert(root,binaryTreeNode(3))
insert(root,binaryTreeNode(6))
insert(root,binaryTreeNode(7))
insert(root,binaryTreeNode(10))
insert(root,binaryTreeNode(1))
print(searchNode(root,3))

