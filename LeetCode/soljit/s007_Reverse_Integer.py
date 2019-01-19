class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        intMax = 2 ** 31 - 1
        intMin = -2 ** 31

        sign = 1

        if x > intMax or x < intMin:
            return 0
        if x < 0:
            sign = -1
            x *= sign

        result = 0
        while x != 0:
            x, lastDigit = divmod(x, 10)
            tempResult = (result * 10) + lastDigit

            # if((tempResult - lastDigit)/10 != result): ## To check overflow
            #     return 0

            result = tempResult

        return 0 if result > intMax or result < intMin else result * sign


