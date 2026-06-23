def coin_change_tab(coins, amount):

    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for target in range(1, amount + 1):

        for coin in coins:

            if target - coin >= 0:

                dp[target] = min(
                    dp[target],
                    1 + dp[target - coin]
                )

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


coins = [1,3,4]
amount = 6

print(coin_change_tab(coins, amount))


