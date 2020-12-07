class Solution:
    ##def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(s: str) -> str:
        lena = len(s)

        ##cache = [[False for x in range(lena)] for y in range(lena)]
        cache = {}
        start, end = 0, 0


        for l in range(lena -1, -1, -1):

            for r in range(l, lena ):

                if l == r : ## One Char Case
                    ##cache[l][r] = True
                    cache[(l,r)] = True
                elif (l + 1 == r and (s[l] == s[r])): ## For 2 Char
                    ##cache[l][r] = True
                    cache[(l,r)] = True
                ##elif (s[l] == s[r] and cache[l+1][r-1] is True ): ## Compare outer letters and inner substrings in cache
                elif (s[l] == s[r] and (l+1,r-1) in cache ):
                    ##cache[l][r] = True
                    cache[(l,r)] = True
                print(cache)
                # Update if it is palindrome and check if length is longer than prev
                ##if( cache[l][r] is True  and (end - start + 1) < (r - l + 1)) :
                if( (l,r) in cache  and (end - start + 1) < (r - l + 1)) :
                    end = r
                    start = l


        return s[start:end+1]




print(Solution.longestPalindrome("aracecarc"))
print(Solution.longestPalindrome("cbbd"))
#print(Solution.longestPalindrome("aba"))