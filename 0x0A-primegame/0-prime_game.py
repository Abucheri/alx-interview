#!/usr/bin/python3
"""
0. Prime Game

Module for determining the winner of multiple rounds of the prime game between
Maria and Ben.

Maria and Ben play a game where they take turns choosing a prime number from a
set of consecutive integers starting from 1 up to and including n. They remove
that number and all its multiples from the set. The player who cannot make a
move loses the game. Maria always goes first, and both play optimally.

Functions:
- isWinner(x, nums): Determines the winner of each round based on
the game's rules.
"""


def findPrimesToN(n):
    """Returns list of primes up to parameter value n, in ascending order.

    Args:
        n (int): the upper bound on list of primes

    Return:
        primes (list) of (int): list of primes to n, or
                                None  on failure

    """

    if (type(n) is not int or n < 0):
        return None

    # logically primes should be a set, but we want it to remain ordered
    primes = []
    for prime_cdt in range(2, n + 1):
        prime = True
        for div in range(2, prime_cdt):
            if (prime_cdt % div == 0):
                prime = False
                break
        if (prime):
            primes.append(prime_cdt)
    return primes


def isWinner(x, nums):
    """
    Determines the winner of a single round of the Prime Game.

    Args:
        n (int): The maximum number of the set of consecutive
                 integers from 1 up to n.

    Returns:
        int: 1 if Maria wins, 2 if Ben wins.
    """
    if (type(nums) is not list or not all([type(n) is int for n in nums]) or
            not all([n > -1 for n in nums])):
        return None

    if (type(x) is not int or x != len(nums)):
        return None

    nums.sort()
    primes = findPrimesToN(nums[-1])
    if (primes is None):
        return None

    Maria_wins = 0
    Ben_wins = 0
    for n in nums:
        prime_ct = 0
        for prime in primes:
            if (prime <= n):
                prime_ct += 1
            else:
                break
        if prime_ct % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1

    if (Maria_wins > Ben_wins):
        return "Maria"
    elif (Ben_wins > Maria_wins):
        return "Ben"
    else:
        return None
