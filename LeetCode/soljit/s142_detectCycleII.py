# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        catchNode = head
        chkNode = head
        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:
                break

        if fast == None or fast.next == None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow