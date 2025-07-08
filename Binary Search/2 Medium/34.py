"""
Leetcode 34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
of a given target value.
If target is not found in the array, return [-1, -1]. You must write
an algorithm with O(log n) runtime complexity.
"""

# Binary search to find the first and last position of the target
def searchRange(nums, target):  
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1  # continue searching in the left half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1  # continue searching in the right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    first_pos = findFirst(nums, target)
    last_pos = findLast(nums, target)
    return [first_pos, last_pos]

# time complexity: O(log n) for both findFirst and findLast
# space complexity: O(1) since we are using a constant amount of space