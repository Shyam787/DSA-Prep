def prefix_sum(nums):

    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]

    return prefix

def query_sum(prefix, left, right):

    if left == 0:
        return prefix[right]
    
    return prefix[right] - prefix[left - 1]

nums = [2, 4, 6, 8, 10]
prefix = prefix_sum(nums)

print(query_sum(prefix, 1, 4))