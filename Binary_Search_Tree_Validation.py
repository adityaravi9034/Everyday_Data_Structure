"""Question:
You are given a binary tree where each node contains an integer value. Write a function to determine if the tree is a binary search tree (BST) or not. 
A binary search tree is a binary tree in which the values of all nodes in the left subtree are less than the value of the root node, and the values of 
all nodes in the right subtree are greater than the value of the root node.


Write a function  isBST(root) that takes the root of the binary tree as input and returns True  if the tree is a binary search tree, and  False otherwise."""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def isBST(root):
    return isBSTHelper(root, float('-inf'), float('inf'))

def isBSTHelper(node, min_val, max_val):
    if node is None:
        return True
    
    if node.val <= min_val or node.val >= max_val:
        return False
    
    return (isBSTHelper(node.left, min_val, node.val) and
            isBSTHelper(node.right, node.val, max_val))

# Example usage:
# Create a binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Check if the tree is a binary search tree
if isBST(root):
    print("The tree is a binary search tree.")
else:
    print("The tree is not a binary search tree.")
