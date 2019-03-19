class Solution:
    def myAtoi(self, pstr):

        ## remove begining spaces
        for id in pstr:
            if (id == ' '):
                pstr = pstr[1:len(pstr)]
            else:
                break

        negFlag = False;

        origLen = len(pstr)

        if (origLen == 0):
            return 0;

        wStr = pstr
        ## check sign and negative flag
        if (pstr[0] == '+' or pstr[0] == '-'):
            if (origLen == 1):
                return 0
            elif pstr[0] == '-':
                negFlag = True

            wStr = pstr[1:origLen]

        res = ''

        for i in wStr:
            if (ord(i) > 47 and ord(i) < 58):
                res = str(res) + str(i)
            else:
                break

        if len(res) == 0: return 0
        nres = int(res)

        ## if number beyond limits
        if (negFlag == True):
            return max(-1 * (2 ** 31), -1 * nres)
        else:
            return min(2 ** 31 - 1, nres)
        """
        :type str: str
        :rtype: int
        """
