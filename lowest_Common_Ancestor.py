"""Question:
You are given a binary tree where each node contains an integer value. Write a function to find the lowest common ancestor (LCA) of two given nodes in the tree. 
The lowest common ancestor is defined as the lowest node in the tree that has both given nodes as descendants.

Write a function lowestCommonAncestor(root, node1, node2) that takes the root of the binary tree and two nodes as input, 
and returns the lowest common ancestor of the two nodes. You may assume that both nodes exist in the tree."""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def lowestCommonAncestor(root, node1, node2):
    if root is None or root == node1 or root == node2:
        return root
    
    left_lca = lowestCommonAncestor(root.left, node1, node2)
    right_lca = lowestCommonAncestor(root.right, node1, node2)
    
    if left_lca and right_lca:
        return root
    elif left_lca:
        return left_lca
    else:
        return right_lca

# Example usage:
# Create a binary tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Define nodes for which to find the lowest common ancestor
node1 = root.left  # Node with value 5
node2 = root.right.right  # Node with value 8

# Find the lowest common ancestor
lca = lowestCommonAncestor(root, node1, node2)
lca_value = lca.val if lca else None
print("Lowest Common Ancestor:", lca_value)
