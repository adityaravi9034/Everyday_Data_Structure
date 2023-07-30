"""You are given an array of integers representing the level-order traversal of a binary search tree (BST). However, the array is missing some elements, and some elements are replaced with -1 as placeholders. Your task is to reconstruct the BST using the provided array.

Write a function reconstruct_bst(level_order) that takes the level-order traversal array as input and returns the root of the reconstructed BST.
Consider the following level-order traversal array:

level_order = [10, 5, 15, 3, -1, 12, -1, -1, -1, 7]
The expected output for this example is a binary search tree with the following structure:

     10
    /   \
   5     15
  /     /
 3     12
  \
   7
Each node in the BST has the following structure:

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

"""


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def reconstruct_bst(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = [root]
    idx = 1

    while idx < len(level_order) and queue:
        node = queue.pop(0)

        left_val = level_order[idx]
        idx += 1
        if left_val != -1:
            node.left = TreeNode(left_val)
            queue.append(node.left)

        if idx < len(level_order):
            right_val = level_order[idx]
            idx += 1
            if right_val != -1:
                node.right = TreeNode(right_val)
                queue.append(node.right)

    return root

# Example usage:
level_order = [10, 5, 15, 3, -1, 12, -1, -1, -1, 7]
root = reconstruct_bst(level_order)
