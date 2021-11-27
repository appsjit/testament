class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrom = ''
        L = len(s)
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        ## Diagonal to 1 ie as single letter is always Palindrome
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]

        for i in range(L - 1, -1, -1):
            # j starts from the i location : to only work on the upper side of the diagonal from bottom
            for j in range(i + 1, L):
                if s[i] == s[j]:  # if the chars mathces
                    ## j-i==1 if next to diagonal
                    ## dp[i+1][j-1] check if inner character was palindrome eg.  dabad when on d check if a is marked True
                    if j - i == 1 or dp[i + 1][j - 1] == True:
                        dp[i][j] = True
                        if len(longest_palindrom) < len(s[i:j + 1]):
                            longest_palindrom = s[i:j + 1]

                            ##print(dp)
        return longest_palindrom