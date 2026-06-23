MOD = 1_000_000_007


def solve(n, L, R, arr):

    total = 0
    streak = 0

    for num in arr:

        # valid element
        if L <= num <= R:

            streak += 1

            # all valid subarrays ending here
            total = (total + streak) % MOD

        else:
            # invalid breaks streak
            streak = 0

    return total


# DRIVER CODE

n = int(input())

L = int(input())
R = int(input())

arr = list(map(int, input().split()))

print(solve(n, L, R, arr))