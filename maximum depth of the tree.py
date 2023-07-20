"""Question:
You are given a binary tree where each node contains an integer value. Write a function to determine the maximum depth of the tree, 
which is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Write a function maxDepth(root) that takes the root of the binary tree as input and returns the maximum depth of the tree."""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def maxDepth(root):
    if root is None:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return max(left_depth, right_depth) + 1

# Example usage:
# Create a binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Calculate the maximum depth of the tree
depth = maxDepth(root)
print("Maximum depth of the tree:", depth)
