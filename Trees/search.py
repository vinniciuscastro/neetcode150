"""
Leetcode 700. Search in a Binary Search Tree

Given the root node of a binary search tree (BST) and a value to search, return the subtree rooted with that value. If the value does not exist in the BST, return null.
Definition for a binary tree node.
"""

 # Pseudo code:
    # def searchBST(self, root, val):
    #     """
    #     :type root: Optional[TreeNode]
    #     :type val: int
    #     :rtype: Optional[TreeNode]
    #     """
    #     if root == null:
    #         return root

    #     if val > root.val:                                                                                                                                                                                                                                                                                                                                    
    #         return searchBST(root.right, val)
    #     if val < root.val:
    #         return searchBST(root.left, val)

    #     return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root: TreeNode, val: int) -> TreeNode:
    if root == None:
        return root

    if val > root.val:
        return searchBST(root.right, val)
    if val < root.val:
        return searchBST(root.left, val)

    return root