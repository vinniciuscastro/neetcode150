def isPalindrome1(s: str) -> bool:
    """
    Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward
    (ignoring spaces, punctuation, and capitalization).
    """
    # Initialize two pointers
    left, right = 0, len(s) - 1

    # Loop until the two pointers meet in the middle
    while left < right:
        # Move the left pointer to the next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move the right pointer to the previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the characters at the two pointers (case insensitive)
        if s[left].lower() != s[right].lower():
            return False

        # Move both pointers inward
        left += 1
        right -= 1

    return True
    
    # time complexity: O(n), where n is the length of the string
    # space complexity: O(1), since we are using only a constant amount of space for the pointers

def isPalindrome2(s: str) -> bool:
    """
    Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward
    (ignoring spaces, punctuation, and capitalization).
    """
    # Using String Concatenation and Slicing
    # Create a new string placeholder
    new_string = ""

    # Loop through the original string
    for char in s:
        # Check if the character is alphanumeric
        if char.isalnum():
            # Append the lowercase version of the character to the new string
            new_string += char.lower()
    # Return True if the new string is equal to its reverse
    return new_string == new_string[::-1]

    # time complexity: O(n), where n is the length of the string
    # space complexity: O(n), since we are creating a new string with the filtered characters
import re
def isPalindrome3(s: str) -> bool:
    """
    Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward
    (ignoring spaces, punctuation, and capitalization).
    """
    # Using Regular Expressions
    # Remove all non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Return True if the string is equal to its reverse
    return s == s[::-1]

    # time complexity: O(n), where n is the length of the string
    # space complexity: O(n), since we are creating a new string with the filtered characters

def main():
    s = "Was it a car or a cat I saw?"
    s2 = "tab a cat"
    print("Two Pointers - Palindrome Check")
    print("------------------------------------------------\n")
    print("Is Palindrome?") 

    print(s + f" - {isPalindrome1(s)}")
    print(s2 + f" - {isPalindrome1(s2)}")
    print("\nConcatenation and Slicing - Palindrome Check")
    print("------------------------------------------------\n") 
    print("Is Palindrome?")
    print(s + f" - {isPalindrome2(s)}")
    print(s2 + f" - {isPalindrome2(s2)}")
    print("\nRegular Expressions - Palindrome Check")
    print("------------------------------------------------\n")
    print("Is Palindrome?")
    print(s + f" - {isPalindrome3(s)}")
    print(s2 + f" - {isPalindrome3(s2)}")

if __name__ == "__main__":
    main()

