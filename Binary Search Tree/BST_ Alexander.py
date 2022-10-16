class Node:
    def __init__(self, key, value):
        self.left_child = None
        self.right_child = None
        self.key = key
        self.value = value
        #self.combo = {self.key: self.value}

    # Insert method to create nodes
    def insert(self, key, value):
        if self.key:
            if key < self.key:
                if self.left_child is None:
                    self.left_child = Node(key, value)
                else:
                    self.left_child.insert(key, value)
            elif key > self.key:
                if self.right_child is None:
                    self.right_child = Node(key, value)
                else:
                    self.right_child.insert(key, value)
        else:
            self.key = key
            self.value = value

    # get method to compare the value with nodes
    def get(self, name):
        if name < self.key:
            if self.left_child is None:
                return str(name) + " Not Found"
            return self.left_child.get(name)
        elif name > self.key:
            if self.right_child is None:
                return str(name) + " Not Found"
            return self.right_child.get(name)
        else:
            return str(self.value)


tree = Node("Vahe", 55)
tree.insert("Thomas", 45)
tree.insert("Zeke", 123)
tree.insert("Al", 23)
tree.insert("Vahy", 66)

#root.insert("Vahe")  # is skipped as it is already implemented

print(tree.get("Thomas"))
print(tree.get("Vahe"))
print(tree.get("Zeke"))
print(tree.get("Al"))
print(tree.get("Alex")) # should return "Alex is not found"