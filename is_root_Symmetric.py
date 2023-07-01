"""You are given a binary tree where each node contains an integer value. Write a function to determine if the tree is symmetric.
A symmetric tree is defined as a tree that is a mirror reflection of itself, i.e., the left subtree of each node is a mirror image of the right subtree.

Write a function isSymmetric(root) that takes the root of the binary tree as input and returns True if the tree is symmetric, and False otherwise."""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def isSymmetric(root):
    if root is None:
        return True
    
    return isMirror(root.left, root.right)

def isMirror(node1, node2):
    if node1 is None and node2 is None:
        return True
    
    if node1 is None or node2 is None:
        return False
    
    if node1.val != node2.val:
        return False
    
    return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

# Example usage:
# Create a symmetric binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

# Check if the tree is symmetric
if isSymmetric(root):
    print("The tree is symmetric.")
else:
    print("The tree is not symmetric.")
