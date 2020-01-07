class Solution:
    def numberToWords(self, num: int) -> str:
        print(num)
        if num == 0:
            return "Zero"

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        less_two = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        thousand = ["", "Thousand", "Million", "Billion"]
        self.result = ''

        def threeHelper(pnum):
            if pnum < 20:
                return less_two[pnum]
            elif (pnum >= 20 and pnum < 100):
                tensq, r = divmod(pnum, 10)
                tensres = tens[tensq] + ' ' + less_two[r]
                return tensres.rstrip()
            elif (pnum >= 100 and pnum < 1000):
                hundreadsq, r1 = divmod(pnum, 100)
                hundredres = less_two[hundreadsq] + ' Hundred ' + threeHelper(r1)
                return hundredres.rstrip()

        def processNums(pnum, tcnt):
            tnum, section = divmod(pnum, 1000)
            print(tnum)
            print(section)
            print(tcnt)
            if section > 0:
                self.result = threeHelper(section) + ' ' + thousand[tcnt] + ' ' + self.result
            if tnum > 0:
                processNums(tnum, tcnt + 1)

        processNums(num, 0)
        print(self.result.rstrip())
        return (self.result.rstrip())
