#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def helper(n):
    """summary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """

    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p] is True:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    prime_list = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_list


def prime_count(n):
    """summary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """

    primes = helper(n)
    return len(primes)


def isWinner(n, numbers):
    """summary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """

    if n < 1 or not numbers:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in numbers:
        primes = prime_count(n)
        if primes % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
