class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))

        longestLength = 1
        dp = {}
        for word in words:
            curLen = 1

            for i in range(len(word)):
                ## Delete one char and check if it exist in map
                tWord = word[:i] + word[i + 1:]
                # Default 0 if does not exist
                prevLen = dp.get(tWord, 0)
                # Add one and compare
                curLen = max(curLen, prevLen + 1)

            dp[word] = curLen

            longestLength = max(longestLength, curLen)

        return longestLength