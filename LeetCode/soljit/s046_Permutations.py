class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backTrack(first=0):
            if first == s:
                result.append(nums[:])

            for x in range(first, s):
                nums[first], nums[x] = nums[x], nums[first]
                backTrack(first + 1)
                nums[first], nums[x] = nums[x], nums[first]
            print(nums)

        s = len(nums)
        result = []
        backTrack()
        return result


