def knapsack(W, wt, val):
    dp = [0] * (W + 1)

    for i in range(len(val)):
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - wt[i]] + val[i])

    return dp[W]


capacity = 8
profits = [1, 2, 5, 6]
weights = [2, 3, 4, 5]

print("Maximum profit:", knapsack(capacity, weights, profits))