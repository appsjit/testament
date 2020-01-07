# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(pnode, lvl, maxLvl):
            if not pnode:
                return

            if (maxLvl[0] < lvl):
                result.append(pnode.val)
                maxLvl[0] = lvl
            helper(pnode.right, lvl + 1, maxLvl)
            helper(pnode.left, lvl + 1, maxLvl)

        result = []
        maxLvl = [0]

        helper(root, 1, maxLvl)
        return result
