"""
LeetCode 303. Range Sum Query - Immutable
Given an integer array nums, handle multiple queries of the following type: 

"""

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
# Time complexity for initialization: O(n), where n is the length of the nums array
# Time complexity for sumRange: O(1), since it uses precomputed prefix sums