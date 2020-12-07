class Solution:
    def longestPalindrome(self, s: str) -> int:
        cntDict = Counter(s)
        print(cntDict)

        odd = False
        res = 0;
        for k, v in cntDict.items():
            chk = divmod(v, 2)
            if chk[1] == 0:
                res += v
            else:
                res += 2 * chk[0]

                if not odd:
                    odd = True
                    res += 1

        return res

