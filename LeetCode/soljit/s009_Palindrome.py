class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        inp = x
        myRev = str(abs(inp))[::-1]
        ##print(myRev)
        intMax = 2 ** 31 - 1
        intMin = -2 ** 31

        if x > intMax or x < intMin:
            return False
        if x < 0:
            return False

        #         result = 0
        #         while x != 0:
        #             x, lastDigit = divmod(x, 10)
        #             tempResult = (result * 10) + lastDigit

        #             # if((tempResult - lastDigit)/10 != result): ## To check overflow
        #             #     return 0

        #             result = tempResult

        if (int(myRev) == inp):  ##(int(result) == inp):
            return True
        else:
            return False



