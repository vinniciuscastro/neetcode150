"""
Leetcode 141: Linked List Cycle
Given a linked list, determine if it has a cycle in it. If there is a cycle, 
return true; otherwise, return false. 
"""

class ListNode:
    """
    Definition for singly-linked list. Slow and Fast Pointer Technique (Floyd's Cycle Detection Algorithm).
    This algorithm uses two pointers, one moving at twice the speed of the other.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    # Check if the linked list is empty or has only one node
    if not head or not head.next:
        return False
    # Initialize two pointers, slow and fast
    # Slow pointer moves one step at a time, fast pointer moves two steps at a time
    slow = head
    fast = head
    # Traverse the linked list with both pointers
    # If there is a cycle, the fast pointer will eventually meet the slow pointer
    while fast and fast.next: # Check if fast pointer and its next node are not None
        slow = slow.next  # Move slow pointer one step
        fast = fast.next.next # Move fast pointer two steps

        if slow == fast: # If slow and fast pointers meet, there is a cycle
            return True   # Cycle detected
    # If the fast pointer reaches the end of the list, there is no cycle

    return False

# Time complexity: O(n), where n is the number of nodes in the linked list
# Space complexity: O(1), since we are using only two pointers