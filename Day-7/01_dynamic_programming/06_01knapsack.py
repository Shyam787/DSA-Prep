def knapsack(weights, values, W):

    # dp[cap] = maximum value for capacity cap
    dp = [0] * (W + 1)

    # Process items from back
    for i in range(len(weights)-1, -1, -1):

        # Copy current row
        new_dp = dp[:]

        for cap in range(W + 1):

            # Can take current item
            if weights[i] <= cap:

                new_dp[cap] = max(

                    # Skip item
                    dp[cap],

                    # Take item
                    values[i] + dp[cap - weights[i]]
                )

        dp = new_dp

    return dp[W]


# Test Input
weights = [1,3,4,5]
values = [1,4,5,7]
W = 7

print("Maximum Value:", knapsack(weights, values, W))