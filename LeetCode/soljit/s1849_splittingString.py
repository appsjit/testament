class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(pPrev, pStr):
            print("Prev :" + pPrev + "  pStr:" + pStr)
            if (len(pStr) == 0):
                return True
            for r in range(1, len(pStr) + 1):
                curr = pStr[:r]
                if int(curr) + 1 == int(pPrev) and dfs(curr, pStr[r:]):
                    return True
            return False

        for l in range(1, len(s)):
            print("Initial Loop:" + s[:l] + "     " + s[l:])
            if dfs(s[:l], s[l:]):
                return True

        return False