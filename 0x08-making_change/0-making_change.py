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

    # Initialize a list to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)

    # Base case: no coins are needed to make 0 amount
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
