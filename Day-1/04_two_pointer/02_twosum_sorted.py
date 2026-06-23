def twosum(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left + 1, right + 1]

        elif current_sum < target:
            left += 1
        
        else: 
            right -= 1
    
    return []

nums = [2, 7, 11, 15]
target = 18

print(twosum(nums, target))
        