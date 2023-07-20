"""
Question:
You are given a binary tree where each node contains an integer value. Write a function to find the maximum path sum in the tree. 
A path in the tree is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path sum is the sum of the values of the nodes in the path.

Write a function maxPathSum(root) that takes the root of the binary tree as input and returns the maximum path sum in the tree."""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def maxPathSum(root):
    max_sum = float('-inf')  # Initialize with negative infinity
    maxPathSumHelper(root, max_sum)
    return max_sum

def maxPathSumHelper(node, max_sum):
    if node is None:
        return 0
    
    left_sum = maxPathSumHelper(node.left, max_sum)
    right_sum = maxPathSumHelper(node.right, max_sum)
    
    # Calculate the maximum sum considering the current node
    current_sum = node.val + max(left_sum, 0) + max(right_sum, 0)
    
    # Update the maximum path sum if the current sum is greater
    max_sum = max(max_sum, current_sum)
    
    # Return the maximum sum starting from the current node
    return node.val + max(max(left_sum, right_sum), 0)

# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Calculate the maximum path sum in the tree
max_sum = maxPathSum(root)
print("Maximum Path Sum:", max_sum)
