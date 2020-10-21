"""
Points-to-ponder:
--> Understand the recursive behaviour of algorithms
--> To 
"""


# A utility class that represents an individual node in a BST 
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 

# A utility function to insert a new node with the given key 
def insert(root,node): 
	if root is None: 
		root = node 
	else: 
		if root.val < node.val: 
			if root.right is None: 
				root.right = node 
			else: 
				insert(root.right, node) 
		else: 
			if root.left is None: 
				root.left = node 
			else: 
				insert(root.left, node) 

# A utility function to do inorder tree traversal 
def inorder(root): 
	if root: 
		inorder(root.left) 
		print(root.val) 
		inorder(root.right)

def preorder(root):
	if root:
		print(root.val)
		preorder(root.left)
		preorder(root.right)

def levelorder(root,level):
	if root is None:
		return
	if level==1:
		print(root.val,end=" ")
		return
	elif level > 1:
		# print(f"level:{level}")
		levelorder(root.left,level-1)
		levelorder(root.right,level-1)

def height(root):
	if root is None:
		return 0
	else:
		lheight = height(root.left)
		rheight = height(root.right)
		if lheight > rheight :
			return lheight+1
		else:
			return rheight+1
# def swap_element(root):

def inorder_with_level(root,level):
	if root:
		inorder_with_level(root.left,level+1)
		print(f"node: {root.val} level:{level}")
		inorder_with_level(root.right,level+1)

# def delete(root,key):

	
# Driver program to test the above functions 
# Let us create the following BST 
#	 50 
# /	 \ 
# 30	 70 
# / \ / \ 
# 20 40 60 80 
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

# Print inoder traversal of the BST 
# print("Inorder: ")
# inorder(r) 
# print("Preorder: ")
# preorder(r)
# print("Level Order: ")
# levelorder(r,3)
# print(height(r))
inorder_with_level(r,1)
