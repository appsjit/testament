class Solution:
    def findLHS(self, nums: List[int]) -> int:

        numsSorted = sorted(nums)
        print(numsSorted)
        indx = 0
        indMin = None
        maxLen = 0
        while indx < len(numsSorted):
            curVal = numsSorted[indx]
            changeStarter = None
            if indMin is not None:
                changeStarter = indMin
                while (changeStarter <= indx):
                    print(changeStarter)
                    ## Update change starter if next higher number starts
                    if numsSorted[indx] - numsSorted[changeStarter] > 1:
                        changeStarter += 1
                    else:
                        break
            ## After initialize assign 0
            indMin = changeStarter if changeStarter is not None else indx

            if (numsSorted[indx] - numsSorted[indMin]) == 1:
                maxLen = max(maxLen, indx - changeStarter + 1)

            print(str(indx) + ":" + str(curVal) + " indMin:" + str(indMin))
            indx += 1
        return maxLen