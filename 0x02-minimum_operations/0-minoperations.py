#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def minOperations(n):
    """
    Description
    """
    if n == 1:
        return 1

    operations = 0
    for i in range(2, n + 1):
        if n % i == 0:
            operations += 1
            n = n // i
            break

    if n > 1:
        operations += n

    return operations
