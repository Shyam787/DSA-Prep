def solve(n, arr):

    prefix_max = [0] * n
    suffix_min = [0] * n

    # build prefix max
    prefix_max[0] = arr[0]

    for i in range(1, n):
        prefix_max[i] = max(
            prefix_max[i - 1],
            arr[i]
        )

    # build suffix min
    suffix_min[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(
            suffix_min[i + 1],
            arr[i]
        )

    # find partition
    for i in range(n - 1):

        if prefix_max[i] <= suffix_min[i + 1]:
            return i + 1


# DRIVER CODE

n = int(input())

arr = list(map(int, input().split()))

print(solve(n, arr))