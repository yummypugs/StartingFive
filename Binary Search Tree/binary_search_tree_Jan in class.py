class Node():
    def __init__(self, key):
        self.key = key
        self.left_children = None
        self.right_children = None

    def insert(self, node):
        # Caveat: Please also handle duplicates.
        if self.key <= node.key:
            self.left_children = node
        else: 
            self.right_children = node

    def delete():
        pass

    def get():
        pass

root_node = Node(4)
print(root_node.key)
print(root_node.left_children)
print(root_node.right_children)