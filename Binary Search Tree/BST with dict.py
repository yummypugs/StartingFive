class Node:
    def __init__(self, key, data):
        self.left = None
        self.right = None
        self.key = key
        self.data = data
        self.combo = {self.key: self.data}

    # Insert method to create nodes
    def insert(self, key, data):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key, data)
                else:
                    self.left.insert(key, data)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key, data)
                else:
                    self.right.insert(key, data)
        else:
            self.key = key
            self.data = data

    # get method to compare the value with nodes
    def get(self, name):
        if name < self.key:
            if self.left is None:
                return str(name) + " Not Found"
            return self.left.get(name)
        elif name > self.key:
            if self.right is None:
                return str(name) + " Not Found"
            return self.right.get(name)
        else:
            print(str(self.data))


root = Node("Vahe", 55)
root.insert("Thomas", 45)
root.insert("Zeke", 123)
root.insert("Al", 23)
root.insert("Vahy", 66)
#root.insert("Vahe")  # is skipped as it is already implemented

root.get("Thomas")
root.get("Vahe")
root.get("Zeke")
root.get("Al")
root.get("Alex")