from collections import deque


def solve(n, k, arr):

    max_dq = deque()
    min_dq = deque()

    left = 0
    best = 0

    for right in range(n):

        # maintain decreasing max deque
        while max_dq and arr[max_dq[-1]] < arr[right]:
            max_dq.pop()

        max_dq.append(right)

        # maintain increasing min deque
        while min_dq and arr[min_dq[-1]] > arr[right]:
            min_dq.pop()

        min_dq.append(right)

        # invalid window
        while arr[max_dq[0]] - arr[min_dq[0]] > k:

            # remove outdated indices
            if max_dq[0] == left:
                max_dq.popleft()

            if min_dq[0] == left:
                min_dq.popleft()

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