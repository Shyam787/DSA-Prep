def longest_consecutive(nums):

    set_nums = set(nums)
    longest = 0

    for num in set_nums:

        if num -1 not in set_nums:
            current = num
            length = 1

            while current +1 in set_nums:
                length += 1
                current += 1
            
            longest = max(longest, length)

    return longest

nums = [100, 2, 4, 3, 200, 1, 5, 6]    
print(longest_consecutive(nums))