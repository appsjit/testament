from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        ns, np = len(s), len(p)
        if ns < np:
            return []
        patCnt = Counter(p)
        strCnt = Counter()
        #         def checkAnagram(idx):
        #             wordCheck = s[idx:idx+len(p)]
        #             s_counter = Counter(wordCheck)

        #             # for x in p:
        #             #     if x not in wordCheck:
        #             #         return
        #             if patCnt == s_counter:
        #                 result.append(idx)

        #         for i in range(len(s) + 1 -len(p)) :
        #             wordCheck = s[i:i+len(p)]
        #             s_counter = Counter(wordCheck)
        #             if patCnt == s_counter:
        #                 result.append(i)

        for i in range(ns):
            strCnt[s[i]] += 1  ## Add Letter to right
            ## If total letters in current window greater than length of p
            if (sum(strCnt.values()) > np):
                if strCnt[s[i - np]] == 1:  ## If only one letter then remove
                    del strCnt[s[i - np]]
                else:  ## subtract counter by 1
                    strCnt[s[i - np]] -= 1

            if strCnt == patCnt:  ## If counter matches add to rsult
                result.append(i - np + 1)

        return result