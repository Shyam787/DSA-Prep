from bisect import bisect_right

def job_scheduling(start, end, profit):

    # combine and sort by end
    jobs = sorted(zip(start, end, profit), key = lambda x : x[1])

    # collect all end times
    ends = [job[1] for job in jobs]

    n = len(start)

    # dp gives max profit upto i
    dp = [0] * n
    dp[0] = jobs[0][2]

    for i in range(1, n):

        current_profit = jobs[i][2]

        # find last non-overlapping job
        j = bisect_right(ends, jobs[i][0]) - 1

        # if valid previous job exists
        if j != -1:
            current_profit += dp[j]

        # take max: skip current job OR take current job
        dp[i] = max(dp[i - 1], current_profit)

    return dp[-1]

# Test Case 1
start =  [1, 2, 3, 3]
end =    [3, 4, 5, 6]
profit = [50, 10, 40, 70]

print("Test Case 1 Output:")
print(job_scheduling(start, end, profit))

# Expected: 120

        
