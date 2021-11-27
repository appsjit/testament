class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

#         def bsHelper(pL, pR):
#             if pR < pL:
#                 return -1
#             if nums[pL] == target:
#                 return pL

#             mid = pL + round(pR - pL/2)
#             midVal = nums[mid-1]

#             if target < midVal:
#                 return bsHelper(pL, mid)
#             else:
#                 return bsHelper(mid, pR)

#             return -1
#         return bsHelper(0, len(nums)-1)






