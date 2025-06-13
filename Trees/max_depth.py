"""
Leetcode 104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
Definition for a binary tree node.  
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(h), where h is the height of the tree (due to recursion stack)