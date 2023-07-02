"""You are given a binary tree where each node contains an integer value. Write a function to find the maximum width of the tree, 
which is the maximum number of nodes in any level.

Write a function maxWidth(root) that takes the root of the binary tree as input and returns the maximum width of the tree."""

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def maxWidth(root):
    if root is None:
        return 0
    
    max_width = 0
    queue = deque([(root, 1)])  # (node, index) tuple to track node position
    
    while queue:
        level_size = len(queue)
        _, start_index = queue[0]  # Starting index of current level
        
        for _ in range(level_size):
            node, index = queue.popleft()
            relative_index = index - start_index + 1
            
            if node.left:
                queue.append((node.left, 2 * relative_index - 1))
            
            if node.right:
                queue.append((node.right, 2 * relative_index))
        
        # Calculate the width of the current level
        width = relative_index if level_size > 1 else 1
        max_width = max(max_width, width)
    
    return max_width

# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

# Calculate the maximum width of the tree
max_width = maxWidth(root)
print("Maximum Width of the Tree:", max_width)
