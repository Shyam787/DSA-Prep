def erase_overlap_intervals(intervals):

    # edge case
    if not intervals:
        return 0, []
    
    # sort by end time
    intervals.sort(key = lambda x : x[1])

    # initialize non overlapping intervals
    non_overlapping = [intervals[0]]
    prev_end = intervals[0][1]
    removals = 0

    # greedy traversal
    for i in range(1, len(intervals)):

        current_start = intervals[i][0]
        current_end = intervals[i][1]

        # if overlaps
        if current_start < prev_end:
            removals += 1

        else: 
            non_overlapping.append(intervals[i])
            prev_end = current_end

    return removals, non_overlapping

# Test Case 1
intervals = [[1,2], [2,3], [3,4], [1,3]]

removals, remaining = erase_overlap_intervals(intervals)

print("Test Case 1")
print("Removals Needed:", removals)
print("Remaining Intervals:", remaining)

# Expected:
# Removals = 1
# Remaining intervals can be:
# [[1,2], [2,3], [3,4]]


print()


# Test Case 2
intervals = [[1,2], [1,2], [1,2]]

removals, remaining = erase_overlap_intervals(intervals)

print("Test Case 2")
print("Removals Needed:", removals)
print("Remaining Intervals:", remaining)

# Expected:
# Removals = 2
# Remaining = [[1,2]]


print()


# Test Case 3
intervals = [[1,2], [2,3]]

removals, remaining = erase_overlap_intervals(intervals)

print("Test Case 3")
print("Removals Needed:", removals)
print("Remaining Intervals:", remaining)

# Expected:
# Removals = 0


print()


# Test Case 4
intervals = [[1,100], [11,22], [1,11], [2,12]]

removals, remaining = erase_overlap_intervals(intervals)

print("Test Case 4")
print("Removals Needed:", removals)
print("Remaining Intervals:", remaining)

# Expected:
# Removals = 2