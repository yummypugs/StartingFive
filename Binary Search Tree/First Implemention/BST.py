class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # findval method to compare the value with nodes
    def get(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.get(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.get(lkpval)
        else:
            print(str(self.data) + ' is found')


root = Node("Vahe")
root.insert("Thomas")
root.insert("Zeke")
root.insert("Al")
root.insert("Vahe")  # is skipped as it is already implemented
root.insert("Vahy")
print(root.get("Thomas"))
