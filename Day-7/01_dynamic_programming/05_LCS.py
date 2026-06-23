def lcs(i, j, s1, s2, dp):

    # Base Case
    if i == len(s1) or j == len(s2):
        return 0

    # Already computed
    if dp[i][j] != -1:
        return dp[i][j]

    # Characters match
    if s1[i] == s2[j]:

        dp[i][j] = 1 + lcs(i + 1, j + 1, s1, s2, dp)

    # Characters do not match
    else:

        dp[i][j] = max(
            lcs(i + 1, j, s1, s2, dp),
            lcs(i, j + 1, s1, s2, dp)
        )

    return dp[i][j]


# Test Input
s1 = "abcde"
s2 = "ace"

m = len(s1)
n = len(s2)

# DP Table
dp = [[-1 for _ in range(n)] for _ in range(m)]

# Answer
print("LCS Length:", lcs(0, 0, s1, s2, dp))

# DP Table Output
print("\nDP Table:")

for row in dp:
    print(row)