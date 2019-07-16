import string
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen = len(s)
        pLen = len(p)
        if (sLen == 0 or pLen == 0):
            return False

        if (pLen < sLen):
            return False

        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}

        dp = [[False] * (pLen) for i in range(sLen)]

        dp[0][0] = True;

        #         for i in range(0,len(s) +1 ):
        #             dp[i][0] = True

        # for j in range(0,pLen):
        #     if p[j] == "*":
        #         dp[0][j] = dp[0][j-1]

        for i in range(sLen):
            for j in range(pLen):

                if (p[j] == "." or p[j] == s[i]):
                    dp[i][j] = True  ##dp[i-1][j-1]
                elif (p[j] == "*"):
                    dp[i][j] = dp[i][j - 1]
                    if (s[i] == p[j - 1] or p[j - 1] == "."):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False

        ## . Printing Matrix
        for j in range(0, len(p)):
            for i in range(0, len(s)):
                print("%5d " % (dp[i][j]), end="")
            print('\n')


        for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
            print(letter1 + letter2)

        if (dp[len(s) - 2][len(p) - 1] == dp[len(s) - 1][len(p) - 1]):
            return False
        return dp[len(s) - 1][len(p) - 1]



