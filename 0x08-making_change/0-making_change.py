#!/usr/bin/python3
"""
This module contains a function to solve the coin change problem
using a dynamic programming approach.

Summary:
    - Validation: The function starts by validating the inputs and handling
                  trivial cases.
    - Sorting: It sorts the coins in descending order to try and minimize
               the number of coins used through a greedy approach.
    - Greedy Calculation: It uses a greedy approach to try and minimize
                          the number of coins, iterating through the sorted
                          coins and updating the remaining amount and the
                          count of coins used.
    - Final Check: Finally, it checks if the total amount was successfully
                   formed and returns the result accordingly.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    If total is 0 or less, the function returns 0 because no coins are needed.
    The function then checks if total is an integer and if coins is a list of
    integers. If the validation fails, it prints "Invalid args" and returns 0.
    This ensures that the inputs are correctly formatted. The coins list is
    sorted in descending order. This is to optimize the solution by trying
    to use larger denominations first, which can sometimes reduce the
    number of coins needed more quickly (a greedy strategy). total_coins
    is initialized to 0 to keep track of the number of coins used.
    rem (remaining amount) is initialized to the total amount that needs
    to be formed. The function iterates through each coin denomination (dm)
    in the sorted list. If the denomination is less than or equal to the
    remaining amount (rem), it calculates how many coins of that denomination
    can be used (current), adds this to total_coins, and subtracts the
    equivalent value from rem. If at any point rem becomes 0,
    the loop breaks because the total amount has been formed. After the loop,
    if no coins were used (total_coins == 0) or there is still a remaining
    amount that couldn't be formed (rem != 0), the function returns -1,
    indicating that it is not possible to form the total amount with
    the given coins. Otherwise, it returns the total_coins, which is the
    minimum number of coins needed to form the total amount.

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
