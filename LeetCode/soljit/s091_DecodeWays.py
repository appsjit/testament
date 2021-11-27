class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        # 226
        # 2 26
        # 2 2 6
        # 22 6

        #   dp  0   0   0   0
        L = len(s)
        res = 0
        dp = [0] * (L + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1

        #   dp  1   1   0   0
        for i in range(2, L + 1):
            # Check if single digit possible
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            # Check 2 digit possible
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]
        # print(dp)
        #   dp  1   1   2   3
        return dp[L]
