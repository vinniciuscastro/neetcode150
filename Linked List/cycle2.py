"""
Medium Question: Leetcode 142 - Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
"""
class ListNode:
    """
    Resolution: Slow and Fast Pointer Technique (Floyd's Cycle Detection Algorithm)
    This algorithm uses two pointers, one moving at twice the speed of the other."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  
    def detectCycle(head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        # Detect cycle using Floyd's Tortoise and Hare algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Cycle detected, find the entry point
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry