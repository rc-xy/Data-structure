"""
This program implements a binary search tree that has functions according to assignment descriptions.

Student number: 20146359
Student name: Xinyu Chen
Date: Mar 5, 2021
"""

# reference to creating BST: https://stackoverflow.com/questions/5444394/how-to-implement-a-binary-search-tree-in-python

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Reference: CISC 235 Red and Black Tree implementation tutorial
    def is_a_leaf(self):
        if self.value == None:
            return True
        else:
            return False


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.weight = []
        self.totalHeight = 0

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.rec_insert(self.root, key)

    def rec_insert(self, node, key):
        if key > node.val:
            if node.right == None:
                node.right = Node(key)
            else:
                self.rec_insert(node.right, key)
        else:
            if node.left == None:
                node.left = Node(key)
            else:
                self.rec_insert(node.left, key)

    # This function with its helper function returns the sum of all nodes' height in the tree.
    def getTotalHeight(self, node):
        # If the node has no children
        if node == None:
            return 0
        else:
            self.totalHeight = self.getTotalHeight(node.left) + self._getTotalHeight(node) + self.getTotalHeight(node.right)
            return self.totalHeight

    def _getTotalHeight(self, node):
        # If the tree is empty
        if node == None:
            return -1
        else:
            return max(self._getTotalHeight(node.left), self._getTotalHeight(node.right))+1
            

    # To implement the getWeightBalanceFactor, I referenced the way to get the size of a tree.
    # Reference to getting the size of a tree: https://www.geeksforgeeks.org/write-a-c-program-to-calculate-size-of-a-tree/
    def getWeightBalanceFactor(self):
        if self.root == None:
            return None
        else:
            self._getWeightBalanceFactor(self.root)
            return max(self.weight)

    def _getWeightBalanceFactor(self, node):
        if node == None:
            return 0
        else:
            left = self._getWeightBalanceFactor(node.left)
            right = self._getWeightBalanceFactor(node.right)
            self.weight.append(abs(right-left))

        # '1' is the size for the node itself if it is not null.
        return self._getWeightBalanceFactor(node.left) + 1 + self._getWeightBalanceFactor(node.right) 
        

    # reference code to printing out BST: https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/

    def print2DUtil(self, node, space):
        if node == None:
            return
        space += 5
        self.print2DUtil(node.right, space)
        print()
        for i in range(5, space):
            print(end=" ")
        print(node.val)

        self.print2DUtil(node.left, space)

    def print2D(self, node):
        self.print2DUtil(node, 0)


if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.insert(6)
    tree.insert(4)
    tree.insert(9)
    tree.insert(5)
    tree.insert(8)
    tree.insert(7)

    print("Total height:", tree.getTotalHeight(tree.root))
    print("Balance factor", tree.getWeightBalanceFactor())
    print("\nBinary tree:\n")
    tree.print2D(tree.root)

