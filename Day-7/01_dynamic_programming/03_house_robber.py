def rob_memo(i, nums, dp):

    # base case 
    if i >= len(nums):
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    take = nums[i] + rob_memo(i + 2, nums, dp)
    skip = rob_memo(i + 1, nums, dp)

    dp[i] = max(take, skip)

    return dp[i]

nums = [2, 7, 9, 3, 1]
dp = [-1] * len(nums)
print(rob_memo(0, nums, dp))


# tabulation
def rob_tab(nums):

    n = len(nums)

    dp = [0] * (n + 2)

    for i in range(len(nums) - 1, -1, -1):

        take = nums[i] + dp[i + 2]
        skip = dp[i + 1]

        dp[i] = max(take, skip)

    return dp[0]

print(rob_tab(nums))


# space optimization
def rob_opt(nums):

    next1 = 0
    next2 = 0

    for i in range(len(nums) - 1, -1, -1):

        curr = max(nums[i] + next2, next1)

        next2 = next1
        next1 = curr

    return next1

print(rob_opt(nums))
