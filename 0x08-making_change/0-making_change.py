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

    if len(coins) == 0:
        return -1

    coins = sorted(coins)
    dm = [float('inf')] * (total + 1)
    dm[0] = 0

    for num in range(total + 1):
        for coin in coins:
            if coin > num:
                break
            if dm[num - coin] != -1:
                dm[num] = min(dm[num - coin] + 1, dm[num])

    if dm[total] == float('inf'):
        return -1

    return dm[total]
