# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None:
            return False

        cnode = head
        jumper = head.next

        while cnode != jumper:
            if (jumper == None or jumper.next == None):
                return False

            cnode = cnode.next
            jumper = jumper.next.next

        return True

