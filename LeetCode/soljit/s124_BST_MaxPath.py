# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxCalc = float('-inf')

        def traverse(trnode):
            if not trnode:
                return 0

            leftVal = max(0, traverse(trnode.left))
            rightVal = max(0, traverse(trnode.right))

            sum = leftVal + rightVal + trnode.val

            self.maxCalc = max(self.maxCalc, sum)

            return max(leftVal, rightVal) + trnode.val

        traverse(root)

        return self.maxCalc


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxNum = -float('inf')

    def traverse(self, root: TreeNode):
        if not root:
            return 0
        left_val = max(Solution.traverse(self, root.left), 0)
        right_val = max(Solution.traverse(self, root.right), 0)

        totNode = root.val + left_val + right_val
        Solution.maxNum = max(Solution.maxNum, totNode)
        return root.val + max(left_val, right_val)

    def maxPathSum(self, root: TreeNode) -> int:
        Solution.maxNum = -float('inf')
        Solution.traverse(self, root)
        return Solution.maxNum

