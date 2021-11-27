class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        for x in range(1, len(nums)):
            if (nums[x - 1] > nums[x]):
                if modified:
                    return False
                modified = True
                if (x < 2 or nums[x - 2] <= nums[x]):
                    nums[x - 1] = nums[x]
                else:
                    nums[x] = nums[x - 1]

        return True
