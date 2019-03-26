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