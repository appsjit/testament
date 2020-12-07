
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def getNm(l):
        x=""
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

            l2,val2=[l2.next , l2.val] if l2 else [0,0]
            hatcha , baki =divmod(val1 + val2 + hatcha , 10)
            result.append(baki)

        return result





    ### Using LinkedList
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            preHead = ListNode(-1)

            res = preHead
            rem = 0
            while l1 != None and l2 != None:
                newNum = l1.val + l2.val + rem
                rem = 0
                if newNum < 10:
                    newNum = newNum
                else:
                    rem = 1
                    newNum -= 10
                newNode = ListNode(newNum)
                res.next = newNode
                res = res.next
                l1 = l1.next
                l2 = l2.next

            remList = l1 if l1 is not None else l2

            while remList != None:
                newNum = remList.val + rem
                rem = 0
                if newNum < 10:
                    newNum = newNum
                else:
                    rem = 1
                    newNum -= 10
                res.next = ListNode(newNum)
                res = res.next
                remList = remList.next

            if rem > 0:
                res.next = ListNode(rem)

            return preHead.next













