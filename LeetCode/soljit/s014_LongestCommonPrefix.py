import sys


class Solution:

    def getCommonStr(w1, w2):
        if (len(w1) == 0):
            return ""

        if (len(w1) > len(w2)):
            w1l = list(w1)
            w2l = list(w2)
        else:
            w1l = list(w2)
            w2l = list(w1)

        cmprOut = ""
        for c in range(len(w2l)):
            if (w2l[c] == w1l[c]):
                cmprOut = cmprOut + w2l[c]
            else:
                return cmprOut

        return cmprOut

    def longestCommonPrefix(self, strs):

        if (len(strs) == 0):
            return ""

        result = strs[0]

        for w in range(len(strs)):
            if (w != 0):
                result = Solution.getCommonStr(result, strs[w])

        return result

        """
        :type strs: List[str]
        :rtype: str
        """


# Trie Solution
# class Solution:
#     wordCurrentCntr = 0
#
#     def processPat(p_tree, p_pat):
#         global wordCurrentCntr
#         patLvl = 0
#         for p in p_pat:
#             if patLvl in p_tree:
#                 childDict = p_tree.get(patLvl)
#                 if p not in childDict:
#                     Solution.wordCurrentCntr = Solution.wordCurrentCntr + 1
#                     ##patLvl = wordCurrentCntr
#                     childDict[p] = Solution.wordCurrentCntr
#                     p_tree[patLvl] = childDict
#                 patLvl = childDict.get(p)
#             else:
#                 childDict = dict()
#                 childDict[p] = patLvl + 1
#                 p_tree[Solution.wordCurrentCntr] = childDict
#                 Solution.wordCurrentCntr = Solution.wordCurrentCntr + 1
#                 patLvl = patLvl + 1
#             ##print(p);
#         return p_tree
#
#     def longestCommonPrefix(strs):
#
#         tree = dict()
#         for pat in strs:
#             tree = Solution.processPat(tree, pat)
#
#         result = ""
#         for node in tree:
#             ##print(node)
#             if (len(tree[node]) == 1):
#                 for c in tree[node]:
#                     result += c
#             else:
#                 return result
#         return result
#
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#
#
# if __name__ == '__main__':
#     strs = ["dog", "racecar", "car"]
#     ##strs = ["flower","flow","flight"]
#     print(Solution.longestCommonPrefix(strs))
#
