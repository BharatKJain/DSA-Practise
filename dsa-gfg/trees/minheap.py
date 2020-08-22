from binarytree import Node

# BST insertion
def insert(root: Node, node: Node) -> Node:
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
                insert(root.right, node)

# min-heap insertion
def minheap_insert(root: Node, node: Node) -> Node:
    if root is None:
        root=node
    else:
        if 
