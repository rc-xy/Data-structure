"""
This program implements an AVL tree map according to the description in assignment 2.

Student number: 20146359
Student name: Xinyu Chen
Date: March 5, 2021
"""

class Node:
    def __init__(self, key=None, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 1
        self.weight = None


class AVLTreeMap:
    def __init__(self):
        self.root = None

    # The function returns the value if the given key exists in the AVL tree based on assignment requirements. 
    def get(self, key):
        if self.root == None:
            return None
        return self._get(self.root, key)

    def _get(self, node, key):
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return None

    # To insert a new key-value pair into the tree
    def put(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if key > node.key:
            if node.right == None:
                node.right = Node(key, value)
                node.right.parent = node
            else:
                node.right = self._put(node.right, key, value)
        elif key < node.key:
            if node.left == None:
                node.left = Node(key, value)
                node.left.parent = node
            else:
                node.left = self._put(node.left, key, value)
        else:
            print("Duplicate values!")

        self.reassign_height_weight(node)
        return self.rebalance(node)

    # The following functions are made to implement the basic functionalities of an AVL tree.

    # Update the node's height after putting a new pair into the tree

    # Reference to simplifying the structure of updating height and weight of an AVL tree: https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/balancedtree/AVLTreeRecursive.java
    def getHeight(self, node):
        if node != None:
            return node.height
        return 0
    
    def reassign_height_weight(self, node):
        node.height = max(self.getHeight(node.left),
                          self.getHeight(node.right)) + 1
        node.weight = self.getHeight(node.right) - self.getHeight(node.left)

    # Rebalance nodes after insertion 
    def rebalance(self, node):
        # Left heavy subtree
        # Case 1 - Left Left
        if node.weight < -1 and node.left.weight <= 0: 
            return self.left_left(node)
        
        # Case 2 - Left Right
        elif node.weight < -1 and node.left.weight > 0:
            return self.left_right(node)

        # Right heavy subtree
        # Case 3 - Right Right
        elif node.weight > 1 and node.right.weight >= 0: 
            return self.right_right(node)
        
        # Case 4 - Right Left
        elif node.weight > 1 and node.right.weight < 0:
            return self.right_left(node)

        # The tree is balanced already.
        return node


    # rotation functions

    # Case 1 - Left Left
    def left_left(self, node):
        return self.right(node)

    # Case 2 - Left Right
    def left_right(self, node):
        return self.left_left(node)

    # Case 3 - Right Right
    def right_right(self, node):
        return self.left(node)

    # Case 4 - Right Left
    def right_left(self, node):
        return self.right_right(node)

    # Perform left rotation
    def left(self, node):
        pivot = node.right
        node.right = pivot.left
        pivot.left = node

        self.reassign_height_weight(node)
        self.reassign_height_weight(pivot)

        return pivot

    # Perform right rotation
    def right(self, node):
        pivot = node.left
        node.left = pivot.right
        pivot.right = node

        self.reassign_height_weight(node)
        self.reassign_height_weight(pivot)

        return pivot

    # Reference to deletion: https://www.techiedelight.com/deletion-from-bst/
    # Remove duplicate nodes
    def remove(self, value):
        if self.Get(value) != None:
            return self._remove(self.Get(value))
        else:
            print("Value of the node is not in the tree.")
            return None

    def _remove(self, node):
        if node == None:
            print("The node does not exist.")
            return None

        # Node has no child.
        if node.left == None and node.right == None:
            if node.parent != None:
                # If the node that needs to be removed equals to the left child, remove the left child.
                if node.parent.left == node:
                    node.parent.left = None
            else:
                self.root = None

        # Node has 2 child.
        elif node.left != None and node.right != None:
            # Find the minimum value in right subtree
            bottom_left = self._bottom_left(node.right)
            node.key = bottom_left.key

            self._remove(bottom_left)
            return

        # Node has 1 children.
        # In lecture note, the following situation is case 2, however, to simplify the if-else statement, I chose it to put it as the third case. 
        else:
            if node.left != None:
                child = node.left
            else:
                child = node.right

            if node.parent != None:
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
            else:
                self.root = child

            child.parent = node.parent

        if node.parent:
            node.parent.height = max(self.getHeight(
                node.parent.left), self.getHeight(node.parent.right)) + 1

    # To get the minimum value 
    def _bottom_left(self, cur_node):
        while cur_node.left != None:
            cur_node = cur_node.left
        return cur_node

    # To find the key in the tree
    def Get(self, key):
        if self.root == None:
            return None
        return self._Get(self.root, key)

    def _Get(self, node, key):
        if key == node.key:
            return node
        elif key < node.key:
            return self._Get(node.left, key)
        elif key > node.key:
            return self._Get(node.right, key)
        else:
            return None

    # Reference code to printing out BST: https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
    def print2DUtil(self, node, space):
        if node == None:
            return
        space += 5
        self.print2DUtil(node.right, space)
        print()
        for i in range(5, space):
            print(end=" ")
        print(node.key, "-", str(node.value))

        self.print2DUtil(node.left, space)

    def print2D(self, root):
        self.print2DUtil(root, 0)


if __name__ == "__main__":
    tree = AVLTreeMap()

    # Put keys and values into the AVL tree
    tree.put(15, "bob")
    tree.put(20, "anna")
    tree.put(24, "tom")
    tree.put(10, "david")
    tree.put(13, "david")
    tree.put(7, "ben")
    tree.put(30, "karen")
    tree.put(36, "erin")
    tree.put(25, "david")

    tree.print2D(tree.root)    # Print out the AVL tree

    print("*---------------------*")    # Divider
    print("The corresponding value to key 24:", tree.get(24))    # To return "tom"

