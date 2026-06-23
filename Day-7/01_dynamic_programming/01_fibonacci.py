def fib(n):

    if n <= 1 :
        return n
    
    dp = [0] *  (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):

        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = 6
print("tabulation fib: ", fib(n))



# space optimized
def fib_opt(n):

    if n <= 1 :
        return n
    
    prev2 = 0
    prev1 = 1

    for _ in range(2, n+1):

        curr = prev2 + prev1

        prev2 = prev1
        prev1 = curr

    return prev1

n = 6
print("space fib: ", fib_opt(n))


# memoization
def fib_memo(n, dp):

    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fib_memo(n-2, dp) + fib_memo(n-1, dp)

    return dp[n]

n = 6
dp = [-1] * (n+1)
print("memo fib: ", fib_opt(n))