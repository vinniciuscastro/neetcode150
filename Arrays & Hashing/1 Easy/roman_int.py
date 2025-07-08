"""
Given a roman numeral, convert it to an integer.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

"""

def roman_to_int1(s: str) -> int: # Reverse the string
    """
    Convert the given Roman numeral string to an integer.
    :param s: Roman numeral string
    :return: Integer value of the Roman numeral     
    """

    # Dictionary to hold the values of Roman numerals
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the total value
    total = 0
    prev = 0
    
    # Loop through the string in reverse order
    for i in s[::-1]:
        # Get the value of the current Roman numeral
        current = roman[i]
        # If the current value is less than the previous value, subtract it from the total  
        if current < prev:
            total -= current
        else:
            total += current
            prev = current
    return total
    # time complexity: O(n), where n is the length of the string
    # space complexity: O(1), since we are using a fixed-size dictionary

def roman_to_int2(s: str) -> int: # Without reversing the string
    """
    Convert the given Roman numeral string to an integer.
    :param s: Roman numeral string
    :return: Integer value of the Roman numeral     
    """

    # Dictionary to hold the values of Roman numerals
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the total value
    total = 0
    
    # Loop through the string
    for i in range(len(s)):
        # Get the value of the current Roman numeral
        current = roman[s[i]]
        # If the current value is less than the next value, subtract it from the total  
        if i + 1 < len(s) and current < roman[s[i + 1]]:
            total -= current
        else:
            total += current
    return total
    # time complexity: O(n), where n is the length of the string
    # space complexity: O(1), since we are using a fixed-size dictionary

def roman_to_int3(s: str) -> int: # Using a single loop
    """
    Convert the given Roman numeral string to an integer.
    :param s: Roman numeral string
    :return: Integer value of the Roman numeral
    """
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev = 0
    # Loop through the string
    for i in s:
        # Get the value of the current Roman numeral
        # Convert the character to its corresponding integer value
        current = roman[i]
        # If the current value is greater than the previous value, subtract twice the previous value
        # from the total to account for the previous addition
        if current > prev:
            # If the current value is greater than the previous value, subtract twice the previous value
            # from the total to account for the previous addition
            total += current - 2 * prev
        # Otherwise, add the current value to the total
        # If the current value is less than or equal to the previous value, add it to the total
        else:
            total += current
        prev = current

    return total
    # time complexity: O(n), where n is the length of the string
    # space complexity: O(1), since we are using a fixed-size dictionary

def roman_to_int4(s: str) -> int: # Left-to-right traversal without reversing
    """
    Convert the given Roman numeral string to an integer.
    :param s: Roman numeral string
    :return: Integer value of the Roman numeral
    """
    # Dictionary to hold the values of Roman numerals
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Initialize the total value
    total = 0
    # Loop through the string
    for i in range(len(s) - 1): # why the -1?
        # compare if current value is less than the next value
        if roman[s[i]] < roman[s[i + 1]]:
            # If the current value is less than the next value, subtract it from the total
            total -= roman[s[i]]
        # Else add the current value to the total
        else:
            total += roman[s[i]]
    # Add the last value to the total +  the last character
    return total + roman[s[-1]]

    # time complexity: O(n), where n is the length of the string
    # space complexity: O(1), since we are using a fixed-size dictionary

def roman_to_int5(s: str) -> int: # Using fixed-size array for lookup 
    """
    Convert the given Roman numeral string to an integer.
    :param s: Roman numeral string
    :return: Integer value of the Roman numeral
    """
    # Array to hold the values of Roman numerals
    roman = [0] * 128
    roman[ord('I')] = 1
    roman[ord('V')] = 5
    roman[ord('X')] = 10
    roman[ord('L')] = 50
    roman[ord('C')] = 100
    roman[ord('D')] = 500
    roman[ord('M')] = 1000

    total = 0
    prev = 0

    # Loop through the string
    for i in s:
        # Get the value of the current Roman numeral using its ASCII value as index
        current = roman[ord(i)]
        # If the current value is greater than the previous value, subtract twice the previous value
        # from the total to account for the previous addition
        if current > prev:
            total += current - 2 * prev
        else:
            total += current
        prev = current

    return total    
    # time complexity: O(n), where n is the length of the string
    # space complexity: O(1), since we are using a fixed-size array

# Test cases
def main():
    """
    Main function to test the roman_to_int functions.
    """
    # Sample input
    roman_numerals = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    
    # Call the roman_to_int functions and print the results
    for numeral in roman_numerals:
        print(f"Roman numeral: {numeral}")
        print(f"Integer value (Method 1): {roman_to_int1(numeral)}")
        print(f"Integer value (Method 2): {roman_to_int2(numeral)}")
        print(f"Integer value (Method 3): {roman_to_int3(numeral)}")
        print(f"Integer value (Method 4): {roman_to_int4(numeral)}")
        print(f"Integer value (Method 5): {roman_to_int5(numeral)}")
        print("-" * 50)
    # Test cases for the roman_to_int functions
    assert roman_to_int1("III") == 3
    assert roman_to_int1("IV") == 4 
    assert roman_to_int1("IX") == 9
    assert roman_to_int1("LVIII") == 58
    assert roman_to_int1("MCMXCIV") == 1994
    assert roman_to_int2("III") == 3
    assert roman_to_int2("IV") == 4
    assert roman_to_int2("IX") == 9
    assert roman_to_int2("LVIII") == 58
    assert roman_to_int2("MCMXCIV") == 1994
    assert roman_to_int3("III") == 3
    assert roman_to_int3("IV") == 4
    assert roman_to_int3("IX") == 9
    assert roman_to_int3("LVIII") == 58
    assert roman_to_int3("MCMXCIV") == 1994
    assert roman_to_int4("III") == 3
    assert roman_to_int4("IV") == 4
    assert roman_to_int4("IX") == 9
    assert roman_to_int4("LVIII") == 58
    assert roman_to_int4("MCMXCIV") == 1994
    assert roman_to_int5("III") == 3
    assert roman_to_int5("IV") == 4
    assert roman_to_int5("IX") == 9
    assert roman_to_int5("LVIII") == 58
    assert roman_to_int5("MCMXCIV") == 1994
if __name__ == "__main__":
    main()