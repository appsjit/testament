class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = "+" + s
        p = "+" + p
        sLen = len(s)
        pLen = len(p)
        if (sLen == 0 or pLen == 0):
            return False

        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}

        dp = [[False] * (pLen) for i in range(sLen)]

        dp[0][0] = True;

        #         for i in range(0,len(s) +1 ):
        #             dp[i][0] = True

        for j in range(1, pLen):
            if p[j] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, sLen):
            for j in range(1, pLen):

                if (p[j] == "." or p[j] == s[i]):
                    dp[i][j] = dp[i - 1][j - 1]
                elif (p[j] == "*"):
                    dp[i][j] = dp[i][j - 2]
                    if (s[i] == p[j - 1] or p[j - 1] == "."):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

                        ## . Printing Matrix
        for j in range(0, len(p)):
            for i in range(0, len(s)):
                print("%5d " % (dp[i][j]), end="")
            print('\n')

        # if (dp[len(s) - 2][len(p) - 1] == dp[len(s) - 1][len(p) - 1]):
        #     return False
        return dp[- 1][- 1]
