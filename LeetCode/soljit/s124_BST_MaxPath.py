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

