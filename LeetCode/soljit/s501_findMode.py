# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.prev = float("inf")
        self.cnt = 0
        self.mode_cnt = 0
        rslt = []

        def travHelper(pnode):
            if not pnode:
                return

            travHelper(pnode.left)

            if pnode.val == self.prev:
                self.cnt += 1
            else:
                self.prev = pnode.val
                self.cnt = 1  # Reset sequence

            if self.cnt == self.mode_cnt:
                rslt.append(pnode.val)
            elif self.cnt > self.mode_cnt:
                self.mode_cnt = self.cnt
                rslt.clear()
                rslt.append(pnode.val)

            travHelper(pnode.right)

        travHelper(root)

        print(rslt)

        return rslt




