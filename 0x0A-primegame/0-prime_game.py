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


def isWinner(x, nums):
    """
    Determine the winner of the game for each round.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers n for each round.

    Returns:
        str: Name of the player who won the most rounds ('Maria' or 'Ben').
             If the winner cannot be determined, returns None.
    """
    if (not isinstance(nums, list) or not all(isinstance(n, int)
       for n in nums) or not all(n >= 1 for n in nums)):
        return None

    nums.sort()
    max_n = nums[-1]
    primes = findPrimesToN(max_n)

    if primes is None:
        return None

    Maria_wins = 0
    Ben_wins = 0

    for n in nums:
        prime_ct = sum(1 for prime in primes if prime <= n)
        if prime_ct % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None


def findPrimesToN(n):
    """
    Returns list of primes up to parameter value n, in ascending order.

    Args:
        n (int): upper bound on list of primes returned

    Return:
        primes (list): list of primes to n, or
        None: on failure
    """
    if not isinstance(n, int) or n < 2:
        return None

    primes = []
    for candidate in range(2, n + 1):
        prime = True
        for divisor in range(2, int(candidate**0.5) + 1):
            if candidate % divisor == 0:
                prime = False
                break
        if prime:
            primes.append(candidate)

    return primes
