#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    :param coins: List of integers representing coin denominations.
    :param total: Integer representing the total amount to achieve.
    :return: Fewest number of coins needed to meet the total, or -1 if impossible.
    """
    if total <= 0:
        return 0

    # Initialize a list to track the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed for a total of 0

    # Loop through each coin and update dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total can't be achieved
    return dp[total] if dp[total] != float('inf') else -1
