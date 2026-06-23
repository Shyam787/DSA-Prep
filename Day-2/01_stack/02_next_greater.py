def next_greater_element(nums):

    n = len(nums)
    results = [-1] * n
    stack = []

    for i in range(n):

        while stack and nums[i] > nums[stack[-1]]:

            index = stack.pop()
            results[index] = nums[i]
        
        stack.append(i)

    return results

nums = [2, 1, 4, 3, 5]
print(next_greater_element(nums))

