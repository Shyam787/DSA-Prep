def duplicate_values(nums):
    
    if len(nums) < 1:
        return 'list doesnot exist'
    
    write = 1

    for read in range(1, len(nums)):

        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
        
    return nums[:write]

nums = [1, 2, 2, 3, 4, 4, 5]
print(duplicate_values(nums))


# move zeros to end while preserving the order of the elements 
def move_zeros(nums):

    if len(nums) < 1:
        return 'list doesnot exist'
    
    write = 0

    for read in range(1, len(nums)):

        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
        
    while write < len(nums):

        nums[write] = 0
        write += 1
    
    return nums

nums = [0, 1, 2, 0, 3, 0, 4, 5]
print(move_zeros(nums))
