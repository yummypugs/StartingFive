class Node:
    def __init__(self, key, value):
        """
        Initializes the Node class with a Name (key) and an Age (value) so that it acts like a dictionary when adding
        nodes left or right in the Tree.
        :param key: String, which takes a Name
        :param value: Integer which takes an age
        """
        # this variable accounts for values that are lesser than the key value
        self.left_child = None
        # this variable accounts for the values that are larger than the key value
        self.right_child = None
        self.key = key  # key of node is defined during the initialization
        self.value = value  # value of node which is the corresponding value of the key
        #self.combo = {self.key: self.value}

    # Insert method to create nodes
    # this function is used to enter the remaining elements ( other than the node value) of the list,
    def insert(self, key, value):
        """
        Calling this function on the Node will insert the Name (key) as a child either left or right to the Node. The
        sorting is dictated by the index in the alphabet, i.e. if the root Node is "Vahe", names with a "lower" rank
        like "Thomas" will be inserted as a child to the left, because "T" is ranked lower than "V".
        :param key: String, which takes a Name
        :param value: Integer which takes an age
        :return: returns nothing, changes child nodes
        """
        if self.key:  # this section will be executed if key value of node is already defined during initialization
            if key < self.key:  # if key value defined in the insert function is less than the key value defined
                # during initialization, this section will be executed
                if self.left_child is None:  # if left_child is being defined for the first time, this section will be executed
                    # left_child variable defined during initialization will be assigned key value defined in insert function
                    self.left_child = Node(key, value)
                # if left_child value has already been taken (i.e it has already been defined beforehead by calling
                # insert function), this section will be executed
                else:
                    # a recursive function of insert is defined, so the alrogithm will run back though the insert
                    # function and the value will be stored in the subclass of initially defined left_child value,
                    # so as to form a binary tree
                    self.left_child.insert(key, value)
            elif key > self.key:  # if key value defined in the insert function is greater than the key value defined
                # during initialization, this section will be executed
                if self.right_child is None:  # if right_child is being defined for the first time, this section will
                    # be executed
                    self.right_child = Node(key, value)  # right_child variable defined during initialization will be
                    # assigned key value defined in insert function
                else:  # if right_child value has already been taken (i.e it has already been defined beforehead by
                    # calling insert function), this section will be executed
                    self.right_child.insert(key, value)  # a recursive function of insert is defined, so the
                    # alrogithm will run back though the insert function and the value will be stored in the subclass
                    # of initially defined left_child value, so as to form a binary tree
        else:  # this section will be executed if key value of node has not been defined
            # this is to define key value of node if it has not been defined during initialization
            self.key = key
            self.value = value
    # basically in this algorithm we are creating binary branches about a node key, and are assigning one right and one left node key to that branch, and subsequently we are creating more binary branches to the left and right key ( for which recursion method is used ) which can be called subbranches of the main branch and so on...

    # get method to compare the value with nodes

    def get(self, name):
        """
        The get function inside Node class returns the corresponding age of the Name passed, which is saved as a
        value to its respective key, like a dictionary. The get function will search the BST and compare the searched
        name to the children names, to determine if the searched name is found in the left or right child. Once it has
        found the name, it will return its corresponding age.
        :param name: A string
        :return: Returns the corresponding age to the passed name, or, if the name is not found, will return
        "Name not found"
        """
        # if node key greater than the input string key ( from get function ), then this section will be executed, ( pls note key is string datatype, so comparison will be based on their alphabatical order )
        if name < self.key:
            if self.left_child is None:  # this line is used to present an error message, if left key of node is empty then the get key is not present in the tree
                return str(name) + " Not Found"  # returns the error message that, the key we are looking for is not present in the tree
            return self.left_child.get(name)  # a recursion function which takes left_child key as node and reruns the get function with left_child key as base
        # if node key less than the input string key ( from get function ), then this section will be executed, ( pls note key is string datatype, so comparison will be based on their alphabatical order )
        elif name > self.key:
            if self.right_child is None:  # this line is used to present an error message, if right key of node is empty then the get key is not present in the tree
                return str(name) + " Not Found"  # returns the error message that, the key we are looking for is not present in the tree
            return self.right_child.get(name)  # a recursion function which takes left_child key as node and reruns the get function with left_child key as base
        else:
            return str(self.value)  # if none of the if and else if conditions stated above are true, then the node key we are comparing is the get key value we are looking for, and so the algorithm will return the corresponding value of the get key

    # similarly we are searching for the corresponding value of the key by going through the branches step by step and comparing the node values with the input key


tree = Node("Vahe", 55)
tree.insert("Thomas", 45)
tree.insert("Zeke", 123)
tree.insert("Alexander", 23)
tree.insert("Vahy", 66)
tree.insert("Kirtesh", 24)
tree.insert("Pei", 32)
tree.insert("Carlo", 21)
tree.insert("Namir", 26)
# root.insert("Vahe")  # is skipped as it is already implemented

print(tree.get("Thomas"))  # should return the corresponding value of key Thomas
print(tree.get("Vahe"))
print(tree.get("Zeke"))
print(tree.get("Pei"))
print(tree.get("Alex"))  # should return "Alex is not found"
