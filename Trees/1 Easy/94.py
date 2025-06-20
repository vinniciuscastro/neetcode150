"""
Easy 
LeetCode 94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Recursive approach
def inorderTraversal(root: 'TreeNode') -> list[int]:
    """
    Perform inorder traversal of a binary tree using recursion.
    
    :param root: Root node of the binary tree
    :return: List of node values in inorder
    """
    if not root:
        return []
    
    # Traverse left subtree, visit root, then traverse right subtree
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(n), due to the recursion stack and the output list

# Iterative approach using a stack
def inorderTraversalIterative(root: 'TreeNode') -> list[int]:
    """
    Perform inorder traversal of a binary tree using an iterative approach with a stack.

    :param root: Root node of the binary tree
    :return: List of node values in inorder
    """
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(n), due to the stack used for storing nodes
