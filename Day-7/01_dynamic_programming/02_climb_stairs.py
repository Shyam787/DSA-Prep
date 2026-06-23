def climb(n):

    if n <= 2 :
        return n
    
    dp = [0] *  (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):

        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = 5
print("tabulation climb: ", climb(n))



# space optimized
def climb_opt(n):

    if n <= 2 :
        return n
    
    prev2 = 1
    prev1 = 2

    for _ in range(3, n+1):

        curr = prev2 + prev1

        prev2 = prev1
        prev1 = curr

    return prev1

n = 5
print("space climb: ", climb_opt(n))


# memoization
def climb_memo(n, dp):

    if n <= 2:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = climb_memo(n-2, dp) + climb_memo(n-1, dp)

    return dp[n]

n = 5
dp = [-1] * (n+1)
print("memo climb: ", climb_opt(n))