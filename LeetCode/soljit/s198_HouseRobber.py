class Solution:
    def rob(self, nums: List[int]) -> int:
        lenNums = len(nums)
        if lenNums == 0:
            return 0

        oddCnt, evenCnt = 0, 0

        for i in range(lenNums):
            temp = oddCnt  ## Hold current
            oddCnt = max(evenCnt + nums[i], oddCnt)  ## take max of both
            evenCnt = temp  ## switch alternate even odd

        return oddCnt






