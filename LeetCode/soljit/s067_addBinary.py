class Solution:
    def addBinary(self, a, b):
        c1, c2 = list(a), list(b)
        i1, i2 = len(c1) - 1, len(c2) - 1
        resltStr = ""
        carry = 0

        while (i1 >= 0 or i2 >= 0):
            fst = 1 if (i1 >= 0 and c1[i1]) == '1' else 0
            snd = 1 if (i2 >= 0 and c2[i2]) == '1' else 0
            #             print("carry "+str(carry)+"  fst:"+str(fst)+" snd:"+str(snd) )

            res = carry + fst + snd
            if res == 0:
                carry = 0
                resltStr = str(0) + str(resltStr)
            elif res == 1:
                carry = 0
                resltStr = '1' + str(resltStr)
            elif res == 2:
                carry = 1
                resltStr = '0' + str(resltStr)
            else:
                carry = 1
                resltStr = '1' + str(resltStr)

            i1 -= 1
            i2 -= 1
        if carry == 1:
            resltStr = '1' + str(resltStr)
        return resltStr
        """
        :type a: str
        :type b: str
        :rtype: str
        """

#
# def add_binary_nums(x, y):
#     max_len = max(len(x), len(y))
#
#     x = x.zfill(max_len)
#     y = y.zfill(max_len)
#
#     result = ''
#     carry = 0
#
#     for i in range(max_len - 1, -1, -1):
#         r = carry
#         r += 1 if x[i] == '1' else 0
#         r += 1 if y[i] == '1' else 0
#         result = ('1' if r % 2 == 1 else '0') + result
#         carry = 0 if r < 2 else 1
#
#     if carry != 0: result = '1' + result
#
#     return result.zfill(max_len)
#
#
# print(add_binary_nums('11', '1'))
# print(add_binary_nums('10', '10'))
# print(add_binary_nums('111', '111'))
# print(add_binary_nums('1111111', '1'))