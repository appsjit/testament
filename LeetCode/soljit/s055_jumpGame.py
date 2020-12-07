class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lenNums = len(nums)
        if lenNums <= 1:
            return True
        intRange = []

        for i in range(lenNums):
            intRange.append(i + nums[i])

        # intRange.sorted()
        print(intRange)
        cur, start, end = 0, 0, 0

        while start < lenNums:
            end = max(end, intRange[start])
            if start == end:
                return False
            start += 1

            if start >= lenNums - 1:
                return True


