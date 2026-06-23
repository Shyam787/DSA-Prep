def subarray_sum(nums, k):

    prefix_sum = 0
    count = 0

    freq = {
        0 : 1
    }

    for num in nums:

        prefix_sum += num

        needed = prefix_sum - k
        if needed in freq:
            count += freq[needed]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count

nums = [1, 2, 3]
k = 3
print(subarray_sum(nums, k))