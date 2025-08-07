"""
LeetCode Problem 9: Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
A palindrome is a number that reads the same backward as forward.
"""
# Resolution: Reversing the Number
def isPalindrome(x):
    if x < 0:
        return False
    original = x
    reversed_num = 0    
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return original == reversed_num
# Time complexity: O(log10(n)), where n is the number of digits in x
# Space complexity: O(1), since we are using a constant amount of space

# Resolution: String Conversion
def isPalindromeString(x):
    s = str(x)
    return s == s[::-1] 
# Time complexity: O(n), where n is the number of digits in x
# Space complexity: O(n), due to the string conversion
# Note: The string conversion method is less efficient for large integers compared to the reversing method.