def permutation(nums):

    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():

        # base condition
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):

            if used[i]:
                continue

            # choose
            path.append(nums[i])
            used[i] = True

            # explore
            backtrack()

            # undo
            path.pop()
            used[i] = False
        
    backtrack()

    return result

nums = [2, 3, 4]
print(permutation(nums))


