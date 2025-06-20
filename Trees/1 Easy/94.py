"""
Easy 
LeetCode 94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

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