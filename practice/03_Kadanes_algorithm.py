def solve(n, arr):

    curr_sum = arr[0]
    best_sum = arr[0]

    for i in range(1, n):

        # either start fresh
        # or continue previous subarray
        curr_sum = max(
            arr[i],
            curr_sum + arr[i]
        )

        best_sum = max(best_sum, curr_sum)

    return best_sum


# DRIVER CODE

n = int(input())

arr = list(map(int, input().split()))

print(solve(n, arr))