class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        singleList = ['1', '8', '0']
        pairDict = {'1': '1', '6': '9', '9': '6', '8': '8', '0': '0'}

        def helper(n, size):
            if n == 0:
                return [""]
            if n == 1:
                return singleList

            centaur = helper(n - 2, size)
            result = []
            for c in centaur:
                result.append('1' + c + pairDict['1'])
                result.append('8' + c + pairDict['8'])
                result.append('6' + c + pairDict['6'])
                result.append('9' + c + pairDict['9'])
                if len(c) + 2 < size:  ## for 3 and above
                    result.append('0' + c + pairDict['0'])

            return result

        return helper(n, n)


