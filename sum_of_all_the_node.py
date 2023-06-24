"""Question:
You are given a binary tree where each node contains an integer value. Write a function to calculate the sum of all the nodes in the tree.

Write a function calculateSum(root) that takes the root of the binary tree as input and returns the sum of all the nodes in the tree.

"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def calculateSum(root):
    if root is None:
        return 0
    
    return root.val + calculateSum(root.left) + calculateSum(root.right)

# Example usage:
# Create a binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Calculate the sum of all nodes in the tree
sum_of_nodes = calculateSum(root)
print("Sum of all nodes in the tree:", sum_of_nodes)
