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
    Maria_wins = 0
    Ben_wins = 0
    if (x < 1 or x != len(nums)):
        return None
    for n in nums:
        winner = determine_winner(n)
        if winner == 1:
            Maria_wins += 1
        elif winner == 2:
            Ben_wins += 1
    if Maria_wins == Ben_wins:
        return None
    elif Maria_wins > Ben_wins:
        return "Maria"
    return "Ben"


def determine_winner(n):
    """
    Determines the winner of a single round of the Prime Game.

    Args:
        n (int): The maximum number of the set of consecutive
                 integers from 1 up to n.

    Returns:
        int: 1 if Maria wins, 2 if Ben wins.
    """
    if (n < 1):
        return None
    if (n == 1):
        return (2)
    nums = list(range(n + 1))
    player = 1
    p = 2
    primes = []
    for num in nums:
        if (num % p == 0):
            nums.remove(num)
    primes.append(p)
    p = 3
    while (nums != [1]):
        if (player == 1):
            player = 2
        else:
            player = 1
        for num in nums:
            if (num % p == 0):
                nums.remove(num)
        primes.append(p)
        p += 2
        flag = 1
        while (flag):
            for num in primes:
                if (p % num == 0):
                    p += 2
                    break
            else:
                flag = 0
    if (player == 1):
        return 1
    return 2
