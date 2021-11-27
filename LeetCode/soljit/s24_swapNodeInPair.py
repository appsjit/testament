# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if ((head == None) or (head.next) == None):
            return head

        # Nodes to be swapped
        firstNode = head
        secondNode = head.next

        # Node Swap
        firstNode.next = self.swapPairs(secondNode.next)
        secondNode.next = firstNode

        return secondNode

