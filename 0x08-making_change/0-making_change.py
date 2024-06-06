#!/usr/bin/python3
"""
This module contains a function to solve the coin change problem
using a dynamic programming approach.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): The values of the coins in your possession.
        total (int): The total amount to be formed with the coins.

    Returns:
        int: The fewest number of coins needed to make the total,
             or -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    newValue = total + 1
    stored = {0: 0}

    for num in range(1, total + 1):
        stored[num] = newValue

        for coin in coins:
            current = num - coin
            if current < 0:
                continue

            stored[num] = min(stored[current] + 1, stored[num])

    if stored[total] == total + 1:
        return -1

    return stored[total]
