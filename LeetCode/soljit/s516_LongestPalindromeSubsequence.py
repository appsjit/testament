class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        L = len(s)
        dp = [[0 for _ in range(L)] for _ in range(L)]

        # Populating diagonal to 0
        for i in range(L):
            dp[i][i] = 1

        # Starting from top of diagonal from right bottom
        for i in range(L - 1, -1, -1):
            for j in range(i + 1, L):
                if s[i] == s[j]:  # If matches then previous match count + 2
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:  # Max on either side
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][L - 1]