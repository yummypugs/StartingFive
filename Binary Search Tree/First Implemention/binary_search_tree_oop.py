class Node():
    def __init__(self, key):
        self.key = key
        self.left_children = None
        self.right_children = None
        self.list_=[key]

    def insert(self, key):
        # Caveat: Please also handle duplicates.
        if self.key <= key:
            self.key = insert(self, key)
            # self.left_children = key
            # self.list_.insert(2,key)
        else:
            self.key = insert(self, key)
            # self.right_children = key
            # self.list_.insert(0,key)
        self.list_=[self.left]+[self.key]+[self.right]

    def delete():
        pass

    def get():
        pass

root_node = Node(4)
root_node.insert(5)
root_node.insert(3)

print(root_node.list_)
print(root_node.key)
print(root_node.left_children)
print(root_node.right_children)