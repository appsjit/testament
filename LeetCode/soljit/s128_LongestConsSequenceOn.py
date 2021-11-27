class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #         myDict = {}
        #         for x in nums:
        #             ##myDict[x]=myDict.get(x, 0) + 1
        #             myDict[x]=1

        #         res = 0
        #         for y in nums:
        #             if (y-1) not in myDict.keys():
        #                 cnt = 1
        #                 curNum = y
        #                 while (curNum+1) in myDict.keys():
        #                     curNum += 1
        #                     cnt += 1
        #                 res = max(res, cnt)

        mySet = set(nums)
        res = 0
        for i in nums:
            if (i - 1) not in mySet:
                cnt = 1
                curNum = i

                while (curNum + 1) in mySet:
                    curNum += 1
                    cnt += 1
                res = max(res, cnt)

        return res