from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = s[:]

        wrdDctSet = set(wordDict)
        queue = deque([0])  ## Inintiated to zero
        visited = [0] * len(s)
        while queue:
            start = queue.popleft()
            if visited[start] == 0:  ## Not Visited yet
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wrdDctSet:
                        print(s[start:end])
                        print(end)
                        queue.append(end)  ## Adding for BFS
                        if (end == len(s)):
                            return True
                visited[start] = 1  ## Mark Visited by changing to 1

        return False