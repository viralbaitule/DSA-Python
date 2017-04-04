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

def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data)
	inorder(root.right)

def postorder(root):
	if root==None:
		return
	postorder(root.left)
	postorder(root.right)
	print(root.data)

def deleteNode(root,value):
	if root==None:
		return root
	elif value<root.data:
		root.left=deleteNode(root.left,value)
	elif value>root.data:
		root.right=deleteNode(root.right,value)
	else:
		#case 1: No child
		if root.left==None and root.right==None:
			root=None
			#case 2: one child
		elif root.left==None:
			right=root.right
			del root
			return right
			
		elif root.right==None:
			left=root.left
			del root
			return left
			#case 3: two childs
		else:
			tempdata=findmin(root.right)
			root.data=tempdata
			root.right=deleteNode(root.right,tempdata)
	return root

root=binaryTreeNode(8)
insert(root,binaryTreeNode(3))
insert(root,binaryTreeNode(10))
insert(root,binaryTreeNode(1))
insert(root,binaryTreeNode(6))
insert(root,binaryTreeNode(4))
insert(root,binaryTreeNode(7))
insert(root,binaryTreeNode(14))
insert(root,binaryTreeNode(13))
postorder(root)
print("after delete")
deleteNode(root,6)
postorder(root)

