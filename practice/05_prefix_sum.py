def solve(n, arr):

    total = sum(arr)

    left_sum = 0

    for i in range(n):

        right_sum = total - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1


# DRIVER CODE

n = int(input())

arr = list(map(int, input().split()))

print(solve(n, arr))