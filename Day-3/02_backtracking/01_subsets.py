def subset_with_duplicates(nums):

    nums.sort()
    result = []
    subset = []

    def backtrack(index):

        result.append(subset[:])

        for i in range(index, len(nums)):

            if i > index and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
        
    backtrack(0)

    return result

nums = [1, 2, 2]
print(subset_with_duplicates(nums))
