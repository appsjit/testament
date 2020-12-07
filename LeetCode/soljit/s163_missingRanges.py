class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        if not nums:
            nums = [lower - 1, upper + 1]
        prev = lower - 1
        res = []
        diffChecker = 0

        if nums[-1] < upper + 1:
            nums.append(upper + 1)

        for i in nums:
            diff = i - prev
            if diff > 1:
                if diff == 2:
                    res.append(str(i - 1))
                elif (diff > 2):
                    res.append(str(prev + 1) + "->" + str(i - 1))
            prev = i

        print(res)

        return res