"""You are given a binary search tree (BST) and two integer values, k1 and k2. Your task is to find all the nodes in the BST that have values between k1 and k2, inclusive.

Write a function find_nodes_in_range(root, k1, k2) that takes the root of the binary search tree, k1, and k2 as inputs and returns a list of nodes in the BST that have values between k1 and k2.

"""
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def find_nodes_in_range(root, k1, k2):
    result = []
    dfs(root, k1, k2, result)
    return result

def dfs(node, k1, k2, result):
    if node is None:
        return

    if k1 <= node.val <= k2:
        result.append(node.val)

    if k1 < node.val:
        dfs(node.left, k1, k2, result)

    if node.val < k2:
        dfs(node.right, k1, k2, result)

# Example usage:
# Create a binary search tree
root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(10)

# Find nodes in the range [5, 9]
k1 = 5
k2 = 9
nodes_in_range = find_nodes_in_range(root, k1, k2)
print("Nodes in the range [5, 9]:", nodes_in_range)
