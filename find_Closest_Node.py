"""class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findClosestNode(root, K):
    closest = root
    while root:
        if root.val == K:
            return root
        if abs(root.val - K) < abs(closest.val - K):
            closest = root
        if K < root.val:
            root = root.left
        else:
            root = root.right
    return closest
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findClosestNode(root, K):
    closest = root
    while root:
        if root.val == K:
            return root
        if abs(root.val - K) < abs(closest.val - K):
            closest = root
        if K < root.val:
            root = root.left
        else:
            root = root.right
    return closest
    
# Define the BST
root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.left = TreeNode(5)
root.left.right = TreeNode(12)
root.right.right = TreeNode(25)

# Call the function
result = findClosestNode(root, 7)
print(result.val)  # Output: 5
