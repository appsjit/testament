# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(pnode, plo=float('-inf'), phi=float('inf')):
            if not pnode:
                return True

            if plo >= pnode.val or phi <= pnode.val:
                return False

            if not helper(pnode.left, plo, pnode.val):
                return False

            if not helper(pnode.right, pnode.val, phi):
                return False

            return True

        return helper(root)

