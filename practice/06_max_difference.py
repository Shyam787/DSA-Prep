# As we traverse:

# maintain minimum value seen so far
# compute current profit/difference
# update maximum answer


def solve(n, arr):

    min_so_far = arr[0]

    best = -1

    for i in range(1, n):

        if arr[i] > min_so_far:

            best = max(
                best,
                arr[i] - min_so_far
            )

        min_so_far = min(
            min_so_far,
            arr[i]
        )

    return best


# DRIVER CODE

n = int(input())

arr = list(map(int, input().split()))

print(solve(n, arr))