#!/usr/bin/python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def makeChange(coins, amount):
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if amount <= 0:
        return 0

    coins.sort(reverse=True)
    n = len(coins)
    i = 0
    count = 0
    while i < n and amount > 0:
        if (coins[i] <= amount):
            amount -= coins[i]
            count += 1
        else:
            i += 1
        if amount == 0:
            return count
        return -1
