#!/usr/bin/python3
import sys


def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Convert the command-line argument to an integer,
# call the factorial function, and print the result
f = factorial(int(sys.argv[1]))
print(f)