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

def findmin(root):
	while root.left!=None:
		root=root.left
	return root.data

def findmax(root):
	while root.right!=None:
		root=root.right
	return root.data

def findheight(root):
	if root==None:
		return -1
	leftheight=findheight(root.left)
	rightheight=findheight(root.right)
	return max(leftheight,rightheight)+1

def preorder(root):
	if root==None:
		return
	print(root.data)
	preorder(root.left)
	preorder(root.right)


root=binaryTreeNode(4)
insert(root,binaryTreeNode(3))
insert(root,binaryTreeNode(6))
insert(root,binaryTreeNode(7))
insert(root,binaryTreeNode(10))
insert(root,binaryTreeNode(15))
print(searchNode(root,3))
print(findmin(root))
print(findmax(root))
print(findheight(root))
preorder(root)
