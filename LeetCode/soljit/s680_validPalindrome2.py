class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()

        def chkDefaultPalin(ps):
            ls = ''.join(e for e in ps if e.isalnum()).lower()
            rev = ls[::-1]
            return ls == rev

        res = chkDefaultPalin(s)
        ts = s[:]
        if not res:
            l, r = 0, len(ts) - 1

            while l < r:
                if ts[l] != ts[r]:
                    return chkDefaultPalin(ts[l + 1:r + 1]) or chkDefaultPalin(ts[l:r])
                l += 1
                r -= 1

        print(res)
        return res