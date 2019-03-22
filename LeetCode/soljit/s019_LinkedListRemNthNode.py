# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        def testTraversal(node):
            # Linked List Traveresal
            # start from the head node
            while node != None:
                print(node.val)  ## access the node value
                node = node.next  ## move on to the next node

        result = []

        firstNode = head
        secondNode = head

        count = 1
        while firstNode.next:
            print(str(count) + " .  " + str(firstNode.val))
            count += 1
            firstNode = firstNode.next
            if (count > n + 1):
                print(" .  " + str(secondNode.val))
                secondNode = secondNode.next
        if count == n:
            return head.next
        else:
            secondNode.next = secondNode.next.next
            return head

        ##testTraversal(resNode)
        #  Alternate Solution
        # class Solution:
        #     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #         if not head: return None
        #
        #         dummy_head = ListNode(-1)
        #         dummy_head.next = head
        #         ahead_node = dummy_head
        #         for _ in range(n):
        #             ahead_node = ahead_node.next
        #
        #         following_node = dummy_head
        #         while ahead_node.next is not None:
        #             ahead_node = ahead_node.next
        #             following_node = following_node.next
        #         following_node.next = following_node.next.next
                # return dummy_head.next

