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
    queue = deque([root])  # Initialize the queue with the root node    
    while queue:
        level_size = len(queue)  # Number of nodes at the current level
        level_nodes = []  # List to store values of nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()  # Pop the first node from the queue
            level_nodes.append(node.val)  # Add its value to the current level's list
            if node.left:  # If left child exists, add it to the queue
                queue.append(node.left)
            if node.right:  # If right child exists, add it to the queue
                queue.append(node.right)
        res.append(level_nodes)  # Add the current level's list to the result
    return res  # Return the list of lists containing level order traversal values
