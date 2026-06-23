def can_jump(nums):

    farthest = 0

    for i in range(len(nums)):

        # unreachable index
        if i > farthest:
            return False
        
        farthest = max(farthest, i + nums[i])

    return True

# Test Case 1
nums = [2, 3, 1, 1, 4]
print("Test Case 1:", can_jump(nums))
# Expected: True


# Test Case 2
nums = [3, 2, 1, 0, 4]
print("Test Case 2:", can_jump(nums))
# Expected: False