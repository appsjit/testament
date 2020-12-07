class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def getTruncated(pWord):
            res = []
            for x in pWord:
                if x != '#':
                    res.append(x)
                elif res:
                    res.pop()
            return "".join(res)

        return getTruncated(S) == getTruncated(T)