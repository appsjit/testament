# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = False

    def traverse(self, node, newSum):

        if not node:
            return

        newSum -= node.val
        if (newSum == 0 and not node.left and not node.right):
            self.result = True
        self.traverse(node.left, newSum)
        self.traverse(node.right, newSum)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        ans = 0

        if not root:
            return False

        self.traverse(root, sum)

        return self.result


