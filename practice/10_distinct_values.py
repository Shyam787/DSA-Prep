from collections import defaultdict


def at_most_k(arr, k):

    left = 0
    count = 0

    freq = defaultdict(int)

    distinct = 0

    for right in range(len(arr)):

        if freq[arr[right]] == 0:
            distinct += 1

        freq[arr[right]] += 1

        # invalid window
        while distinct > k:

            freq[arr[left]] -= 1

            if freq[arr[left]] == 0:
                distinct -= 1

            left += 1

        # count valid subarrays
        count += (right - left + 1)

    return count


def solve(n, k, arr):

    return at_most_k(arr, k) - at_most_k(arr, k - 1)


# DRIVER CODE

n, k = map(int, input().split())

arr = list(map(int, input().split()))

print(solve(n, k, arr))