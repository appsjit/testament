class Solution:
    arDict = dict()

    def appendToDict(k, lta):

        if (k in Solution.arDict):
            cList = str(Solution.arDict.get(k))
            if (cList != 'None'):
                Solution.arDict[k] = cList + lta
            else:
                Solution.arDict[k] = lta
        else:
            Solution.arDict[k] = lta

    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        if len(s) <= (numRows - 1):
            return s

        midp = 0
        currun = 0
        for idx in range(len(s)):
            q, r = divmod(idx, (numRows - 1))
            if (r == 0):
                if (q % 2 == 0):
                    Solution.appendToDict(0, s[idx])
                    if (midp == 0):
                        midp += (numRows - 1)
                    else:
                        midp += 2 * numRows - 2
                else:

                    Solution.appendToDict((numRows - 1), s[idx])
                    currun += 1
            else:
                if(idx < (numRows - 1)):
                    Solution.appendToDict(idx, s[idx])
                else:
                    Solution.appendToDict(numRows - 1 - abs(midp - idx) , s[idx])


        result = ""
        for i in range(numRows):
            result += Solution.arDict.get(i)
        return result
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
