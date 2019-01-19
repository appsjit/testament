class Solution:
    def getValRoIn(strng):
        if strng == 'I':
            return 1
        elif strng == 'IV':
            return 4
        elif strng == 'V':
            return 5
        elif strng == 'IX':
            return 9
        elif strng == 'X':
            return 10
        elif strng == 'XL':
            return 40
        elif strng == 'L':
            return 50
        elif strng == 'XC':
            return 90
        elif strng == 'C':
            return 100
        elif strng == 'CD':
            return 400
        elif strng == 'D':
            return 500
        elif strng == 'CM':
            return 900
        elif strng == 'M':
            return 1000
        else:
            return 0

    def romanToInt(self, s):
        print(Solution.getValRoIn('CM'))
        resNum = 0
        pr = 0

        while (pr < len(s)):
            num = Solution.getValRoIn(s[pr])
            if (pr < len(s) - 1):
                nextVal = Solution.getValRoIn(s[pr + 1])
                if (num < nextVal):
                    val = Solution.getValRoIn(s[pr] + s[pr + 1])
                    resNum += val
                    pr += 2
                else:
                    resNum += num
                    pr += 1
            else:
                resNum += num
                pr += 1
        return resNum

        """
        :type s: str
        :rtype: int
        """
