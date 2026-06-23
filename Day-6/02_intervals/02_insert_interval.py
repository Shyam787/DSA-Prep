def insert_interval(intervals, new_interval):

    i = 0
    n = len(intervals)
    result = []

    # phase 1 - add before intervals

    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # phase 2 - merge intervals

    while i < n and intervals[i][0] <= new_interval[1]:

        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])

        i += 1

    # add merged interval
    result.append(new_interval)

    # phase 3 - add after intervals

    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Test Case 2
intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]]
new_interval = [4,8]

print("Test Case 2 Output:")
print(insert_interval(intervals, new_interval))

# Expected:
# [[1,2], [3,10], [12,16]]
