from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = s[:]

        wrdDctSet = set(wordDict)

        ## Solution 1 Using BFS
        # queue = deque([0]) ## Inintiated to zero
        # visited = [0] * len(s)
        # while queue:
        #     start = queue.popleft()
        #     if visited[start] == 0 : ## Not Visited yet
        #         for end in range(start + 1, len(s) + 1):
        #             if s[start:end] in wrdDctSet :
        #                 print(s[start:end])
        #                 print(end)
        #                 queue.append(end) ## Adding for BFS
        #                 if (end == len(s)):
        #                     return True
        #         visited[start] = 1 ## Mark Visited by changing to 1

        ## Solution 2 using DP
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(0, len(s) + 1):
            for j in range(0, i + 1):
                ##print(s[j:i])
                if (dp[j] and s[j:i] in wrdDctSet):
                    dp[i] = True
                    break

        return dp[len(s)]