"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false

Explanation: The brackets are not closed in the correct order.

"""
def is_valid1(s: str) -> bool:
    """
    Check if the input string s is a valid parentheses string.
    A valid parentheses string is one where every open bracket is closed by the same type of close bracket,
    and open brackets are closed in the correct order.

    :param s: Input string containing parentheses characters
    :return: True if the string is valid, False otherwise
    """
    # Dictionary to hold matching pairs of parentheses
    matching = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of open brackets
    stack = []
    
    # Loop through each character in the string
    for c in s:
        # If it's a closing bracket, check if it matches the last opened bracket
        if c in matching:
            if not stack or stack[-1] != matching[c]:
                return False  # Mismatch found or stack is empty
            stack.pop()  # Remove the last opened bracket from the stack
        else:
            stack.append(c)  # Add open brackets to the stack
    
    return not stack  # Return True if all brackets are matched, False otherwis

# Time complexity: O(n)
# Space complexity: O(n)

def is_valid2(s: str) -> bool:
    """
    Check if the input string s is a valid parentheses string.
    A valid parentheses string is one where every open bracket is closed by the same type of close bracket,
    and open brackets are closed in the correct order.

    :param s: Input string containing parentheses characters
    :return: True if the string is valid, False otherwise
    """
    # Dictionary to hold matching pairs of parentheses
    matching = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of open brackets
    stack = []
    
    # Loop through each character in the string
    for c in s:
        # If it's a closing bracket, check if it matches the last opened bracket
        if c in matching:
            if not stack or stack[-1] != matching[c]:
                return False  # Mismatch found or stack is empty
            stack.pop()  # Remove the last opened bracket from the stack
        else:
            stack.append(c)  # Add open brackets to the stack

    return not stack  # Return True if all brackets are matched, False otherwise

# Time complexity: O(n)
# Space complexity: O(n)

def is_valid2(s: str) -> bool: # Brute force
    """
    Check if the input string s is a valid parentheses string.
    A valid parentheses string is one where every open bracket is closed by the same type of close bracket,
    and open brackets are closed in the correct order.

    :param s: Input string containing parentheses characters
    :return: True if the string is valid, False otherwise
    """
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return s == ''

# Time complexity: O(n^2)
# Space complexity: O(n)    

def main():

    test_cases = [
        "[]",
        "([{}])",
        "[(])",
        "((()))",
        "{[()]}",
        "((()))",
        "((())",
        "(()))",
        "([)]",
        "([]{})"
    ]
    print("Test Cases:\n")
    for s in test_cases:
        print(f"Stack Solution = {is_valid1(s)} ~{s}~")
        print(f"Brute Force Solution = {is_valid2(s)} ~{s}~")
        print("-" * 40)


if __name__ == "__main__":
    main()

# This code is designed to check if a string of parentheses is valid.
