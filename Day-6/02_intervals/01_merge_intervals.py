def merge_intervals(intervals):
    
    intervals.sort(key = lambda x : x[0])

    # add first interval
    merged = [intervals[0]]

    # process other intervals
    for current in intervals[1:]:


        last = merged[-1]

        # start time less tham previous end time
        if current[0] <= last[1]:

            # merge
            last[1] = max(last[1], current[1])

        else:

            merged.append(current)

    return merged


# Test Case 1
intervals = [[1,3], [2,6], [8,10], [15,18]]

print("Test Case 1 Output:")
print(merge_intervals(intervals))

# Expected:
# [[1,6], [8,10], [15,18]]


print()


# Test Case 2
intervals = [[1,4], [4,5]]

print("Test Case 2 Output:")
print(merge_intervals(intervals))

# Expected:
# [[1,5]]
