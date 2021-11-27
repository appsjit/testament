# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 1

        def traverseAndCalc(pNode):
            if not pNode: return 0
            L = traverseAndCalc(pNode.left)
            R = traverseAndCalc(pNode.right)

            self.res = max(self.res, L + R + 1)
            return max(L, R) + 1

        traverseAndCalc(root)

        return self.res - 1


