'''
Problem Statement:

Implement a function power(base, exponent) that calculates the result of raising base to the power of exponent (i.e., computes base exponent).

Constraints:

        - Do not use Python's built-in exponentiation operator (**) or the pow() function.
        - You may use basic arithmetic operators: addition (+), subtraction (-), multiplication (*), and division (/).
'''

def power_iterative(base: float, exponent: int) -> float:
    """
    Calculate the power of a base raised to an exponent using iterative multiplication.
    
    :param base: The base number (float)
    :param exponent: The exponent (int)
    :return: The result of base raised to the power of exponent (float)
    """
    if exponent == 0:
        return 1.0  # Any number raised to the power of 0 is 1
    elif exponent < 0:
        base = 1 / base  # Invert the base for negative exponents
        exponent = -exponent
    
    result = 1.0
    for _ in range(exponent):
        result *= base  # Multiply the result by the base for each iteration
    
    return result

def power_recursive(base: float, exponent: int) -> float:   
    """
    Calculate the power of a base raised to an exponent using recursive multiplication.
    
    :param base: The base number (float)
    :param exponent: The exponent (int)
    :return: The result of base raised to the power of exponent (float)
    """
    if exponent == 0:
        return 1.0  # Any number raised to the power of 0 is 1
    elif exponent < 0:
        return 1 / power_recursive(base, -exponent)  # Invert the base for negative exponents
    
    return base * power_recursive(base, exponent - 1)  # Multiply the base by the result of the recursive call


def main(): 
    """
    Test the power functions with some sample input.
    """
    # Sample input
    base = 2
    exponent = 2
    
    # Call the power functions and print the results
    print("-" * 50 + "\n")
    print(f"Base: {base}, Exponent: {exponent}")
    print("Power using iterative method:")
    print(f"Result: {power_iterative(base, exponent)}")
    print("\n--------------------------------------------------\n")
    print(f"Base: {base}, Exponent: {exponent}")
    print("Power using recursive method:")
    print(f"Result: {power_recursive(base, exponent)}")
    print("\n--------------------------------------------------\n")

  
    assert power_iterative(2, 3) == 8
    assert power_iterative(5, 0) == 1
    assert power_iterative(2, -2) == 0.25
    assert power_iterative(-2, 3) == -8

    assert power_recursive(2, 3) == 8
    assert power_recursive(5, 0) == 1
    assert power_recursive(2, -2) == 0.25
    assert power_recursive(-2, 3) == -8

if __name__ == "__main__":
    main()