class Solution:
    def trap(self, height: List[int]) -> int:
        if (height == None):
            return 0

        result = 0
        scr = 0
        blockLen = len(height)
        stack = []

        def peek(stack):
            return stack[len(stack) - 1]

        while scr < blockLen:
            while (len(stack) > 0 and height[scr] > height[peek(stack)]):
                ##print("Working scr:"+str(scr))
                last = peek(stack);
                stack.pop()
                if (len(stack) == 0):
                    break
                dist = scr - peek(stack) - 1
                ## Take minimum between current scroller and remaining latest stack for top level
                ## - removed node height for bottom level
                waterHeight = min(height[scr], height[peek(stack)]) - height[last]
                result += dist * waterHeight

            stack.append(scr)
            scr += 1
            ##print(stack)

        return result


# class Solution:  ## Left right Pointers
#     def trap(self, height: List[int]) -> int:
#         l, r = 0, len(height) - 1
#         lmx, rmx = 0, 0
#         res = 0
#         while l < r:
#             if height[l] < height[r]:
#                 if height[l] >= lmx:
#                     lmx = height[l]
#                 else:
#                     res += lmx - height[l]
#                 l += 1
#             else:
#                 if height[r] >= rmx:
#                     rmx = height[r]
#                 else:
#                     res += rmx - height[r]
#                 r -= 1
#
#         return res


# class Solution:  ## DP Solution
#     def trap(self, height: List[int]) -> int:
#         lmx = []
#         rmx = [0] * len(height)
#         res = 0
#         lc, rc = 0, 0
#         for i in range(len(height)):
#             lc = max(lc, height[i])
#             lmx.append(lc)
#
#         for j in range(len(height) - 1, -1, -1):
#             rc = max(rc, height[j])
#             rmx[j] = rc
#
#         for z in range(len(height)):
#             res += (min(lmx[z], rmx[z]) - height[z])
#
#         return res