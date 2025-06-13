"""
Easy
LeetCoode: 100. Same Tree   
Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # If both nodes are None, they are the same
    if not p and not q:
        return True
    # If one of the nodes is None, they are not the same
    if not p or not q:
        return False
    # If the values of the nodes are different, they are not the same
    if p.val != q.val:
        return False
    # Recursively check the left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Time complexity: O(n), where n is the number of nodes in the trees
# Space complexity: O(h), where h is the height of the trees (due to recursion stack)

# Example usage:
# p = TreeNode(1, TreeNode(2), TreeNode(3))
# q = TreeNode(1, TreeNode(2), TreeNode(3))
# print(isSameTree(p, q))  # Output: True