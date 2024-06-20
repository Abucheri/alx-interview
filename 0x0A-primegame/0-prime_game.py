#!/usr/bin/python3
"""
0. Prime Game

Module for determining the winner of multiple rounds of the prime game between
Maria and Ben.

Maria and Ben play a game where they take turns choosing a prime number from a
set of consecutive integers
starting from 1 up to and including n. They remove that number and all its
multiples from the set. The player who cannot make a move loses the game.
Maria always goes first, and both play optimally.

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
    def sieve_of_eratosthenes(max_num):
        """
        Sieve of Eratosthenes algorithm to find
        all prime numbers up to max_num.

        Args:
            max_num (int): The numer to sieve through.

        Returns:
            list: List of booleans where prime[i] is True
                  if i is a prime number.
        """
        if max_num < 2:
            return []
        is_prime = [True] * (max_num + 1)
        # 0 and 1 are not prime numbers
        is_prime[0] = is_prime[1] = False
        p = 2
        while (p * p <= max_num):
            if (is_prime[p] is True):
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        return is_prime

    def compute_game_outcomes(nums):
        """
        Compute game outcomes for all rounds using precomputed primes.

        Args:
            nums (list): list of precomputed primes.

        Returns:
            list: List where result[i] is True if Maria wins when n = nums[i].
        """
        max_n = max(nums)
        primes = sieve_of_eratosthenes(max_n)
        results = [False] * (max_n + 1)

        for n in range(2, max_n + 1):
            if (primes[n] and not any(results[n - p]
               for p in range(2, n // 2 + 1) if primes[p])):
                results[n] = True
        return results

    results = compute_game_outcomes(nums)
    maria_wins_count = sum(results[n] for n in nums)
    ben_wins_count = x - maria_wins_count

    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
        return "Ben"
    else:
        return None
