class Solution:
    def plusOne(self, digits):
        result = []
        str1 = ''.join(str(e) for e in digits)
        resNum = list(str(int(str1) + 1))

        for x in resNum:
            result.append(int(x))

        return result

    def plusOne2(self, digits): ##self, digits: List[int]) -> List[int]:
        n = len(digits)
        rdigits = digits[:]

        overflow = 0

        for x in range(n - 1, -1, -1):
            res = digits[x] + overflow
            if (x == n - 1):
                res += 1

            if res > 9:
                res = 0
                overflow = 1
            else:
                overflow = 0

            digits[x] = res

            if x == 0 and overflow > 0:
                digits.insert(0, overflow)
        return digits

# class Solution:
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         a = int(''.join(map(str, digits)))
#         a += 1
#         return [int(i) for i in str(a)]


