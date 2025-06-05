"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. 
"""

def two_sum1(nums: list[int], target: int) -> list[int]:
    """
    Find two indices in the array nums such that their corresponding values add up to the target.

    :param nums: List of integers
    :param target: Target integer
    :return: List of two indices
    """
    # Dictionary to store the indices of the numbers
    num_to_index = {}
    
    # Loop through the list of numbers
    for index, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        diff = target - num
        
        # Check if the complement is already in the dictionary
        if diff in num_to_index:
            return [num_to_index[diff], index]  # Return the indices if found
        
        # Store the index of the current number in the dictionary
        num_to_index[num] = index
    
    return []  # Return an empty list if no solution is found

# time complexity: O(n)
# space complexity: O(n)

def two_sum2(nums: list[int], target: int) -> list[int]:
    """
    Find two indices in the array nums such that their corresponding values add up to the target.

    :param nums: List of integers
    :param target: Target integer
    :return: List of two indices
    Brute force approach
    """
    # Loop through the list of numbers
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Check if the sum of the two numbers equals the target
            if nums[i] + nums[j] == target:
                return [i, j]  # Return the indices if found
    
    return []  # Return an empty list if no solution is found
# time complexity: O(n^2)
# space complexity: O(1)

import bisect

def two_sum3(nums: list[int], target: int) -> list[int]:
    """
    Find two indices in the array nums such that their corresponding values add up to the target.

    :param nums: List of integers
    :param target: Target integer
    :return: List of two indices
    Binary search approach
    """
    # Sort the list of numbers and keep track of the original indices
    sorted_nums = sorted((num, i) for i, num in enumerate(nums))
    
    # Loop through the sorted list of numbers
    for i in range(len(sorted_nums)):
        # Calculate the complement needed to reach the target
        diff = target - sorted_nums[i][0]
        
        # Use binary search to find the index of the complement
        j = bisect.bisect_left(sorted_nums, (diff, 0), i + 1)
        
        # Check if the complement is found and its index is different from the current index
        if j < len(sorted_nums) and sorted_nums[j][0] == diff:
            return [sorted_nums[i][1], sorted_nums[j][1]]  # Return the original indices if found
    
    return []  # Return an empty list if no solution is found
# time complexity: O(n log n)
# space complexity: O(n)    



def main():
    """
    Main function to test the two_sum functions.
    """
    # Test cases
    nums = [2, 7, 11, 15]
    target = 18
    
    # Call the two_sum functions and print the results
    print("two_sum (hash_map)      -", two_sum1(nums, target))  # Output: [0, 1]
    print("two_sum (brute force)   -", two_sum2(nums, target))  # Output: [0, 1]
    print("two_sum (binary search) -", two_sum3(nums, target))  # Output: [0, 1]

if __name__ == "__main__":
    main()