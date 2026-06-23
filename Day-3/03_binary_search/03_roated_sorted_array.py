def search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = left + (right - left) // 2

        # found
        if nums[mid] == target:
            return mid
        
        # left half sorted
        if nums[left] <= nums[mid]:

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            
            else:
                left = mid + 1

        # right half sorted    
        else:

            if nums[mid] < target <= nums[right]:
                 left = mid + 1

            else:
                right = mid - 1
    
    return -1

nums = [4, 5, 6, 7, 1, 2, 3]
target = 1

print(search(nums, target))