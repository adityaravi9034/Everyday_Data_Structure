"""
Question:
You are given a binary tree where each node contains an integer value. Write a function to determine if the tree is balanced. A balanced tree is defined as a tree in which the heights of the two subtrees of any node never differ by more than one.

Write a function isBalanced(root) that takes the root of the binary tree as input and returns True if the tree is balanced, and False otherwise."""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def isBalanced(root):
    if root is None:
        return True
    
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    
    if abs(left_height - right_height) > 1:
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)

def getHeight(node):
    if node is None:
        return 0
    
    left_height = getHeight(node.left)
    right_height = getHeight(node.right)
    
    return max(left_height, right_height) + 1

# Example usage:
# Create a binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Check if the tree is balanced
if isBalanced(root):
    print("The tree is balanced.")
else:
    print("The tree is not balanced.")
