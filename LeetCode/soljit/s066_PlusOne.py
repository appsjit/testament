class Solution:
    def plusOne(self, digits):
        result = []
        str1 = ''.join(str(e) for e in digits)
        resNum = list(str(int(str1) + 1))

        for x in resNum:
            result.append(int(x))

        return result



# class Solution:
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         a = int(''.join(map(str, digits)))
#         a += 1
#         return [int(i) for i in str(a)]