class Solution:
    def largestRectangleArea(self, heights) -> int:
        stHeight = 0
        endHeight = 0
        maxArea = 0
        L = len(heights)
        # Initiate stack with -1 index assuming height before index 0 is lowest to begin with
        stack = [-1]
        for i in range(L):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                curHeight = heights[stack.pop()]
                # width formula when next height less than current height
                # i - stack[i] - 1
                curWidth = i - stack[-1] - 1
                maxArea = max(maxArea, curHeight * curWidth)
            stack.append(i)

        ## When no smaller heights at end ie increasing graph
        while stack[-1] != -1:
            curHeight = heights[stack.pop()]
            # width formula for lowest remaining heights
            curWidth = L - stack[-1] - 1
            maxArea = max(maxArea, curHeight * curWidth)

        return maxArea


sol = Solution()
print('Local Testing '+str(sol.largestRectangleArea([2,1,5,6,2,3])))

