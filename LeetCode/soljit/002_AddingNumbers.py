
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def getNm(l): x=""
        childNode = l
        while childNode.next != None:
            x = str(childNode.val)+x
            # print(childNode.val)
            childNode = childNode.next
    # print(childNode.val)
        x = str(childNode.val)+x
        if (x == "" or x == None ):
            x=0
        return int(x)

    def addTwoNumbers(self, l1, l2):
        # resNum = Solution.getNm(l1) + Solution.getNm(l2)
        # return list(map(int, str(resNum)[::-1]))

        """

        :type l1: ListNode

        :type l2: ListNode

        :rtype: ListNode

        """
        hatcha = 0
        result = list()
        while l1 or l2 or hatcha:
            val1 = l1.val if l1 else 0
            l1 = l1.next if l1 else 0

            l2,val2=[l2. next , l2.val] i f l2 else [0,0]
            hatcha , baki =divmod(val1 + val2 + hatcha , 10)
            result.append(baki)

        return result










