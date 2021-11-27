# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = 0

        def traverse(pRoot):
            if not pRoot:
                return (0, 0)

            lval, lcnt = traverse(pRoot.left)
            rval, rcnt = traverse(pRoot.right)
            nonlocal res
            res = max(res, ((lval + rval + pRoot.val) / (lcnt + rcnt + 1)))
            return (lval + rval + pRoot.val), (lcnt + rcnt + 1)

        traverse(root)

        return res
