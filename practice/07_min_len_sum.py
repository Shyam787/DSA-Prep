def solve(n, k, arr):

    left = 0
    curr_sum = 0

    best = float('inf')

    for right in range(n):

        curr_sum += arr[right]

        # valid window
        while curr_sum >= k:

            best = min(
                best,
                right - left + 1
            )

            curr_sum -= arr[left]
            left += 1

    return best if best != float('inf') else -1


# DRIVER CODE

n, k = map(int, input().split())

arr = list(map(int, input().split()))

print(solve(n, k, arr))