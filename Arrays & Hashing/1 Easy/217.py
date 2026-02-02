"""
Leetcode Problem 217: Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

"""
# Using a hashmap to track seen numbers
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create a hashmap to track duplicates
        dupli_check = {}
        # Loop through each number in the array
        for n in nums:
            # If the number is already in the hashmap, we found a duplicate
            if n in dupli_check:
                return True
            # Otherwise, add the number to the hashmap
            else:
                dupli_check[n] = n

        return False

# Time complexity: O(n), where n is the length of the nums array
# Space complexity: O(n) in the worst case if all elements are distinct