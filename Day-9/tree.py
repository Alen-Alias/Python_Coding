class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class BST:
    def __init__(self):
        self.root=None
    def insert(self,data,node=None):
        if self.root is None:
            self.root=Node(data)
            node=self.root
            return
        if node is None:
            node=self.root
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert(data, node.right)
        
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end=" ")
        self.inorder(node.right)
        
t=BST()
t.insert(5)
t.insert(3)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(1)
t.inorder(t.root)
