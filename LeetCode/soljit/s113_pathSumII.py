# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorder(self, node, newSum, temp, result):
        if node == None:
            return

        newSum -= node.val
        temp.append(node.val)

        if (newSum == 0 and not node.left and not node.right):
            result.append(temp[:])

        self.preorder(node.left, newSum, temp, result)
        self.preorder(node.right, newSum, temp, result)

        temp.pop()

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        result = []
        self.preorder(root, sum, [], result)

        return result





