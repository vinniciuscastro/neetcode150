"""
LeetCode 102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its 
nodes' values. (i.e., from left to right, level by level)
"""
# Breath-first search (BFS) approach to perform level order traversal of a binary tree.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode) -> list[list[int]]:
    """Steps to do BFS level order traversal:
    0. Add the root node to a queue.
    1. check the queue size
    2. pop the first element from the queue
    3. add node value to the result list
    4. add the children of the popped node to the queue
    5. repeat steps 1-4 until the queue is empty
    """
    if not root:
        return []
    res = []
