def min_platforms(arrival, departure):

    # sort arrival and departure
    arrival.sort()
    departure.sort()

    n = len(arrival)

    # pointers
    i = 0
    j = 0

    platform = 0
    max_platforms = 0

    while i < n and j < n:

        # a train arrives before departure
        if arrival[i] <= departure[j]:
            platform += 1

            max_platforms = max(max_platforms, platform)

            i += 1

        # a train departure
        else:
            platform -= 1

            j += 1

    return max_platforms

# Test Case 1
arrival =   [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

print("Test Case 1 Output:",
      min_platforms(arrival, departure))


