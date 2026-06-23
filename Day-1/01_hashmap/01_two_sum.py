def two_sum(num, target):
    seen = {}
    
    for i, num in enumerate(num):
        complement = target - num
        
        if complement in seen:
            return f'[{seen[complement]}, {i}]'
        seen[num] = i

num = [2, 4, 8, 1, 5]
target = 6
print(two_sum(num, target))