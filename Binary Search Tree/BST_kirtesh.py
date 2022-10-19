class Node:
    def __init__(self, key, value):
        self.left_child = None # this variable accounts for values that are lesser than the key value
        self.right_child = None # this variable accounts for the values that are larger than the key value
        self.key = key # key of node is defined during the initialization
        self.value = value # value of node which is the corresponding value of the key
        #self.combo = {self.key: self.value}

    # Insert method to create nodes
    def insert(self, key, value): # this function is used to enter the remaining elements ( other than the node value) of the list,
        if self.key: # this section will be executed if key value of node is already defined during initialization
            if key < self.key: # if key value defined in the insert function is less than the key value defined during initialization, this section will be executed
                if self.left_child is None: # if left_child is being defined for the first time, this section will be executed
                    self.left_child = Node(key, value) # left_child variable defined during initialization will be assigned key value defined in insert function
                else:                                 # if left_child value has already been taken (i.e it has already been defined beforehead by calling insert function), this section will be executed
                    self.left_child.insert(key, value)  # a recursive function of insert is defined, so the alrogithm will run back though the insert function and the value will be stored in the subclass of initially defined left_child value, so as to form a binary tree
            elif key > self.key: # if key value defined in the insert function is greater than the key value defined during initialization, this section will be executed
                if self.right_child is None: # if right_child is being defined for the first time, this section will be executed
                    self.right_child = Node(key, value) # right_child variable defined during initialization will be assigned key value defined in insert function
                else:                                   # if right_child value has already been taken (i.e it has already been defined beforehead by calling insert function), this section will be executed
                    self.right_child.insert(key, value) # a recursive function of insert is defined, so the alrogithm will run back though the insert function and the value will be stored in the subclass of initially defined left_child value, so as to form a binary tree
        else:                                          # this section will be executed if key value of node has not been defined
            self.key = key                             # this is to define key value of node if it has not been defined during initialization
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