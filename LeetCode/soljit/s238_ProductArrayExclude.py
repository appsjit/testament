class Solution:
    def productExceptSelf(self, nums): ## List[int]) -> List[int]:
        ls = 0
        rs = len(nums)
        L = []
        R = [0] * rs

        for x in range(rs):
            if x == 0:
                L.append(nums[x])
            else:
                L.append(nums[x] * L[x - 1])

        print(L)
        for x in range(rs - 1, -1, -1):
            if x == (rs - 1):
                R[x] = nums[x]
            else:
                R[x] = R[x + 1] * nums[x]

        print(R)
        result = []
        for r in range(rs):
            lm = r - 1
            rm = r + 1
            ans = 0
            if lm < 0:
                ans = R[rm]
            elif rm > rs - 1:
                ans = L[lm]
            else:
                ans = L[lm] * R[rm]
            result.append(ans)

        return result


