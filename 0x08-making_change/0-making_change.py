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

    if type(total) is not int or type(coins) is not list or not all(
            [type(coin) is int for coin in coins]):
        print("Invalid args")
        return 0

    coins.sort(reverse=True)

    total_coins = 0
    rem = total

    for dm in coins:
        if dm <= rem:
            current = rem // dm
            total_coins += current
            rem -= current * dm
        if rem == 0:
            break

    if total_coins == 0 or rem != 0:
        return -1

    return total_coins
