# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            if l1 == None:
                return l2
            if l2 == None:
                return l1
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

        totLists = len(lists)
        interval = 1

        while interval < totLists:
            for x in range(0, totLists - interval, 2 * interval):
                lists[x] = mergeTwoLists(lists[x], lists[x + interval])
            interval *= 2
            ##print(lists[x])
        return lists[0] if totLists > 0 else lists

        ## Merge 2 Lists first and then add 3rd List to FIrst List
        ## Merge By Divide and Conquer


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def mergeTwo(l1, l2):
            if l1 == None:
                return l2
            if l2 == None:
                return l1

            preHead = ListNode(-1)
            res = preHead

            while l1 and l2:
                if l1.val <= l2.val:
                    res.next = l1
                    l1 = l1.next
                else:
                    res.next = l2
                    l2 = l2.next
                res = res.next

            res.next = l1 if l1 is not None else l2

            return preHead.next

        if len(lists) <= 1:
            return lists

        interval = 1
        while interval < len(lists):
            for x in range(0, len(lists) - interval, interval * 2):
                lists[x] = mergeTwo(lists[x], lists[x + interval])
            interval = interval * 2

        return lists[0] if len(lists) > 0 else lists