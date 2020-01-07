# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        print(root.val)
        self.result = None

        def findClosest(tnode):
            if tnode.val == val:
                left = None
                right = None
                if tnode.left:
                    left = tnode.left.val
                if tnode.right:
                    right = tnode.right.val
                self.result = tnode  ##[tnode.val, left, right]
            if tnode.left and tnode.val > val:
                findClosest(tnode.left)
            if tnode.right and tnode.val < val:
                findClosest(tnode.right)

        findClosest(root)

        return self.result
