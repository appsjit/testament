# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0

        def dfsPO(pnode):
            if not pnode:
                return 'C'
            left = dfsPO(pnode.left)
            right = dfsPO(pnode.right)

            if (left == 'NC' or right == 'NC'):
                self.ans += 1
                return 'CAM'
            return 'C' if (left == 'CAM' or right == 'CAM') else 'NC'

        return (1 if dfsPO(root) == 'NC' else 0) + self.ans
