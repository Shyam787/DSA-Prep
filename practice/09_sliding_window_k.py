def solve(n, k, arr):

    left = 0
    zeros = 0

    best = 0

    for right in range(n):

        if arr[right] == 0:
            zeros += 1

        # invalid window
        while zeros > k:

            if arr[left] == 0:
                zeros -= 1

            left += 1

        best = max(
            best,
            right - left + 1
        )

    return best


# DRIVER CODE

n, k = map(int, input().split())

arr = list(map(int, input().split()))

print(solve(n, k, arr))