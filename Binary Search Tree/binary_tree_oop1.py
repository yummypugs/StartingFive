class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self,data):
        if data<self.data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        elif data>self.data:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.insert(data)


root=Node(5)
root.insert(8)
root.insert(2)
root.insert(6)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(12)
root.insert(7)
def PrintTree(self):
    if self.left:
        self.left.PrintTree()
        print(self.data)
    if self.right:
        self.right.PrintTree()



PrintTree(root)


