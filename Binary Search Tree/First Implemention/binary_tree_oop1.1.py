class Node:
    def __init__(self,data):
        self.left_children=None
        self.right_children=None
        self.data=data

    def insert(self,data):
        if data<self.data:
            if self.left_children is None:
                self.left_children=Node(data)
            else:
                self.left_children.insert(data)
        elif data>self.data:
            if self.right_children is None:
                self.right_children=Node(data)
            else:
                self.right_children.insert(data)


root=Node(5)
root.insert(8)
root.insert(2)
root.insert(6)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(12)
root.insert(7)




PrintTree(root)


