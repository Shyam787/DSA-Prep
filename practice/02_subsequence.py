from bisect import bisect_left


def solve(n, arr):

    tails = []

    for num in arr:

        idx = bisect_left(tails, num)

        # extend LIS
        if idx == len(tails):
            tails.append(num)

        # replace existing tail
        else:
            tails[idx] = num

    return len(tails)


# DRIVER CODE

n = int(input())

arr = list(map(int, input().split()))

print(solve(n, arr))