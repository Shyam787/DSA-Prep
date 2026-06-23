def combination_sum(nums, target):

    result = []
    path = []

    def backtrack(index, remaining):

        # sucess
        if remaining == 0:
            result.append(path[:])
            return
        
        # failure - pruning
        if remaining < 0:
            return
        
        for i in range(index, len(nums)):

            # choose
            path.append(nums[i])

            # explore
            backtrack(i, remaining - nums[i])

            # undo
            path.pop()

    backtrack(0, target)

    return result

nums = [2, 3, 5]
target = 5

print(combination_sum(nums, target))