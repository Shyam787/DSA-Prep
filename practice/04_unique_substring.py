def solve(s):

    left = 0
    best = 0

    seen = set()

    for right in range(len(s)):

        # duplicate found
        while s[right] in seen:

            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        best = max(
            best,
            right - left + 1
        )

    return best


# DRIVER CODE

s = input().strip()

print(solve(s))