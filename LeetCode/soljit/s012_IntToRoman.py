from collections import OrderedDict


class Solution:

    def intToRoman(self, num):
        result = ""
        # TODO convert int to roman string
        roman = OrderedDict()
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"
        ##print(num)
        wNum = num
        for r in roman.keys():

            x, y = divmod(wNum, r)
            print("r:" + str(r) + "  x:" + str(x) + "  y:" + str(y))

            if (x > 0):
                flagNum = r
                print(roman[r] * x)
                result = result + roman[r] * x
                wNum = y

        return result


