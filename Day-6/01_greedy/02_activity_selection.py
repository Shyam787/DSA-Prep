def activity_selection(start, end):
    n = len(start)

    # pair activities
    activities = []

    for i in range(n):
        activities.append((start[i], end[i]))

    # sort by ending time
    activities.sort(key = lambda x : x[1])

    # first activity
    count = 1
    selected_activities = [activities[0]]
    last_end = activities[0][1]

    for i in range(1, n):

        curr_start = activities[i][0]
        curr_end = activities[i][1]

        if curr_start >= last_end:
            count += 1
            selected_activities.append(activities[i])
            last_end = curr_end

    return count, selected_activities

start = [1, 3, 0, 5, 8, 5]
end =   [2, 4, 6, 7, 9, 9]

count, activities = activity_selection(start, end)

print("Maximum Activities:", count)
print("Selected Activities:", activities)