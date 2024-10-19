#!/usr/bin/python3
"""
this module calculates the minimum operation a function needs
"""


def minOperations(n):
    """
    the function is the begining of it all
    """
    if n <= 1:
        return 0  # Impossible to achieve

    operations = 0
    factor = 2  # Start checking factors from 2

    # Factorize n
    while n > 1:
        if n % factor == 0:  # If factor is a divisor
            operations += factor  # Add the factor to operations
            n //= factor  # Reduce n
        else:
            factor += 1  # Move to the next factor

    return operations
