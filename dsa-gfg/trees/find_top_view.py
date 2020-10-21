from collections import deque
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insertNode(root,node):
    if root is None:
        root=node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right=node
            else:
                insertNode(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insertNode(root.left,node)

def fetch(root):
    left_pointer=root.left
    right_pointer=root.right
    values=deque([root.val])
    while left_pointer!=None or right_pointer!=None:
        # print(left_pointer.val)
        # print(right_pointer.val)
        if left_pointer != None:
            values.appendleft(left_pointer.val)
        if right_pointer !=None:
            values.append(right_pointer.val)
        if left_pointer!=None:
            left_pointer=left_pointer.left
        if right_pointer!=None:
            right_pointer=right_pointer.right
    for element in values:
        print(element,end=" ")

def fetch_verticle_traversal(root,level,mem:dict,main_list):
    if root:
        if level in mem:
            mem[level].append(root.val)
        else:
            mem[level]=deque([root.val])
            main_list.append(root.val)
        fetch_verticle_traversal(root.left,level-1,mem,main_list)
        fetch_verticle_traversal(root.right,level+1,mem,main_list)
        

if __name__=="__main__":
    # r = Node(50) 
    # insertNode(r,Node(30)) 
    # insertNode(r,Node(20)) 
    # insertNode(r,Node(40)) 
    # insertNode(r,Node(70)) 
    # insertNode(r,Node(60)) 
    # insertNode(r,Node(80)) 
    # print(fetch(r))
    n=int(input())
    list_nodes=[int(element) for element in input().split(' ')]
    root=Node(list_nodes[0])
    for element in list_nodes[1:]:
        insertNode(root,Node(element))
    # fetch(root)
    memory={}
    main_l=deque([])
    fetch_verticle_traversal(root,0,memory,main_l)
    for key,value in sorted(memory.items()):
        print(value[0]  ,end=" ")
    print()
    print(memory)
    print(main_l)``
