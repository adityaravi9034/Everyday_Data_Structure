"""You are given the root of a binary tree. Your task is to determine if the tree is symmetric around its center, i.e., if it is a mirror of itself when you flip it left to right.

Write a function is_symmetric(root) that takes the root of the binary tree as input and returns True if the tree is symmetric, and False otherwise.

The TreeNode class for representing the binary tree node is provided below:
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

Example:

# Symmetric tree
root1 = TreeNode(1)
root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
root1.right = TreeNode(2, TreeNode(4), TreeNode(3))

# Non-symmetric tree
root2 = TreeNode(1)
root2.left = TreeNode(2, None, TreeNode(3))
root2.right = TreeNode(2, None, TreeNode(3))

result1 = is_symmetric(root1)
result2 = is_symmetric(root2)

print(result1)  # Output: True
print(result2)  # Output: False
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    if not root:
        return True
    return is_mirror(root.left, root.right)

# Example usage:
root1 = TreeNode(1)
root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
root1.right = TreeNode(2, TreeNode(4), TreeNode(3))

root2 = TreeNode(1)
root2.left = TreeNode(2, None, TreeNode(3))
root2.right = TreeNode(2, None, TreeNode(3))

result1 = is_symmetric(root1)
result2 = is_symmetric(root2)

print(result1)  # Output: True
print(result2)  # Output: False
