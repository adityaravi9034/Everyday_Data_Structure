"""
Question:
You are given a binary tree where each node contains an integer value. Write a function to find the diameter of the tree. The diameter of a binary tree is defined as the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

Write a function diameterOfBinaryTree(root) that takes the root of the binary tree as input and returns the diameter of the tree.

"""
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    if root is None:
        return 0
    
    diameter = 0
    max_depth(root, diameter)
    return diameter

def max_depth(node, diameter):
    if node is None:
        return 0
    
    left_depth = max_depth(node.left, diameter)
    right_depth = max_depth(node.right, diameter)
    
    # Update the diameter if the current path is longer
    diameter = max(diameter, left_depth + right_depth)
    
    # Return the maximum depth of the current node's subtree
    return max(left_depth, right_depth) + 1

# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calculate the diameter of the tree
diameter = diameterOfBinaryTree(root)
print("Diameter of the Tree:", diameter)
