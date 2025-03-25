def large_power(base, exponent):
    """
    Determines if raising 'base' to the power of 'exponent' results in a value greater than 5000.

    Parameters:
    base (numeric): The base number.
    exponent (numeric): The exponent to which the base is raised.

    Returns:
    bool: True if (base ** exponent) > 5000, otherwise False.

    Example:
    >>> large_power(10, 4)
    True
    >>> large_power(2, 10)
    False
    """
    
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# test
# print(large_power(10, 4))  # Output: True (10000 is greater than 5000)
# print(large_power(2, 10))  # Output: False (1024 is NOT greater than 5000)




def divisible_by_ten(num):
    """
    Determines if a number is divisible by 10.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if num is divisible by 10, otherwise False.

    Example:
    >>> divisible_by_ten(50)
    True
    >>> divisible_by_ten(37)
    False
    >>> divisible_by_ten(0)
    True
    """

    if num % 10 == 0:
        return True
    else:
        return False
    
# print(divisible_by_ten(50))  # Output: True
# print(divisible_by_ten(37))  # Output: False
# print(divisible_by_ten(0)) # Output: True
