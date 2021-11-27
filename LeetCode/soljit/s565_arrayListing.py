class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        ans = 0

        def checkLongest(pIdx, pMax):
            nonlocal visited
            nonlocal ans
            if visited and pIdx in visited:
                return
            else:
                visited.add(pIdx)
                checkLongest(nums[pIdx], pMax + 1)
                ans = max(ans, pMax)

        for idx, val in enumerate(nums):
            if idx not in visited:
                checkLongest(nums[idx], 1)

        return ans


#######################################################


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        ans = 0

        def checkLongest(pIdx, pMax):
            nonlocal visited

            if visited and pIdx in visited:
                return pMax
            else:
                visited.add(pIdx)
                return checkLongest(nums[pIdx], pMax + 1)

        for idx, val in enumerate(nums):
            if idx not in visited:
                ans = max(ans, checkLongest(nums[idx], 0))

        return ans


#######################################################
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        ans = 0

        def checkLongest(pIdx):
            nonlocal visited
            length = 0
            while pIdx not in visited:
                visited.add(pIdx)
                pIdx = nums[pIdx]
                length += 1

            return length

        for idx, val in enumerate(nums):
            if idx not in visited:
                ans = max(ans, checkLongest(nums[idx]))

        return ans