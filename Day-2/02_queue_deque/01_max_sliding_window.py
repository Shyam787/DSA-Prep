from collections import deque

def max_sliding_window(nums, k):

    dq = deque()
    results = []

    for i in range(len(nums)):

        # removing expired indices
        while dq and dq[0] <= i - k:
            dq.popleft()

        # remove dominated candidates
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        dq.append(i)

        # window formed
        if i >= k -1:
            results.append(nums[dq[0]])
        
    return results

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(max_sliding_window(nums, k))
