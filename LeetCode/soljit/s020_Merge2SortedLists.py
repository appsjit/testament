# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def printLi(pL):
        trL = pL
        while trL != None:
            print(trL.val)
            trL = trL.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        ##prev.next = l1 if l1 is not None else 12        ## throws error
        prev.next = l1 if l1 is not None else l2  ## works

        return prehead.next