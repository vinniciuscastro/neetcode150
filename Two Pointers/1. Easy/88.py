"""
LeetCode 88 . Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted
array.The number of elements initialized in nums1 and nums2 are m and n respectively. 
You may assume that nums1 has a size equal to m + n such that it has enough
space to hold additional elements from nums2.
"""
# Resolution: Two Pointers from the End
def merge(nums1, m, nums2, n):
    x, y = m-1, n-1

    for i in range(m+n -1, -1, -1):
        ind_x = nums1[x]
        
        if y < 0:
            break  
        ind_y =  nums2[y]  
        if x < 0:
            nums1[i] = ind_y
            y -= 1 
        
        elif ind_x > ind_y:
            nums1[i] = ind_x
            x -= 1 
        else:
            nums1[i] = ind_y
            y -= 1
    return nums1
# Time complexity: O(m + n), where m and n are the lengths of nums1 and nums2
# Space complexity: O(1), since we are modifying nums1 in place

