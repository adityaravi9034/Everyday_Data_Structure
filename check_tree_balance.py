# Checking if a binary tree is height balanced

from Trees.BinaryTree import Node


def height(tree):
    if tree is None:
        return 0
    else:
        return 1 + max(height(tree.leftChild), height(tree.rightChild))


def isBalanced(tree):

    # if binary tree is empty
    if tree is None:
        return True

    # get the height of left and right subtree
    left_height = height(tree.leftChild)
    right_height = height(tree.rightChild)

    # recursively check all the subtree
    if abs(left_height - right_height) <= 1 and isBalanced(tree.leftChild) and isBalanced(tree.rightChild):
        return True

    # return false if the tree in not balanced
    return False


if __name__ == "__main__":
    r = Node('a')
    r.insertLeft('b')
    r.leftChild.insertLeft('d')
    r.leftChild.insertRight('e')
    r.leftChild.rightChild.insertLeft('f')
    r.leftChild.rightChild.insertRight('g')
    r.insertRight('c')
    r.rightChild.insertRight('h')
    r.rightChild.rightChild.insertRight('i')

    if isBalanced(r):
        print('The tree is balanced')
    else:
        print('The tree is not balanced')
