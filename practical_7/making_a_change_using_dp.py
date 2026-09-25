# Practical 7
# Implementation of Making Change Problem
# using Dynamic Programming

def coin_change(coins, amount):

    # dp[i] = minimum number of coins needed for amount i
    dp = [float('inf')] * (amount + 1)

    # selected[i] = coin used to make amount i
    selected = [0] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):

        for coin in coins:

            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                selected[i] = coin

    # If change cannot be made
    if dp[amount] == float('inf'):
        return -1, []

    # Find the coins used
    result = []
    current = amount

    while current > 0:
        coin = selected[current]
        result.append(coin)
        current -= coin

    return dp[amount], result


# Main program
print("MAKING CHANGE USING DYNAMIC PROGRAMMING")
print("-" * 45)

coins = [1, 2, 5, 10]
amount = 18

minimum_coins, used_coins = coin_change(coins, amount)

print("Available coins:", coins)
print("Amount:", amount)

if minimum_coins == -1:
    print("Change cannot be made.")
else:
    print("Minimum number of coins required:", minimum_coins)
    print("Coins used:", used_coins)