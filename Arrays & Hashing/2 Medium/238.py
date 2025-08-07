"""
Leetcode 238. Given an array nums of n integers where n > 1, 
return an array output such that output[i] is equal to the product of all 
the elements of nums except nums[i]. 
"""
# Resolution: Prefix and Suffix Product Arrays
def productExceptSelf(nums):
    n = len(nums)
    # Initialize output array with 1s
    output = [1] * n   
    prefix = 1
    suffix = 1  
    # Calculate prefix products
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]   
    # Calculate suffix products
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]   
    return output   

# Time complexity: O(n), where n is the number of elements in the input array
# Space complexity: O(1), since we are using the output array for results   

# Resolution: Using prefix and suffix products to avoid division   