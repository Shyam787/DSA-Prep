from collections import defaultdict


def solve(n, k, arr):

    prefix_count = defaultdict(int)

    # important for subarrays starting at index 0
    prefix_count[0] = 1

    curr_sum = 0
    answer = 0

    for num in arr:

        curr_sum += num

        needed = curr_sum - k

        answer += prefix_count[needed]

        prefix_count[curr_sum] += 1

    return answer


# DRIVER CODE

n, k = map(int, input().split())

arr = list(map(int, input().split()))

print(solve(n, k, arr))