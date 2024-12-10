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
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
