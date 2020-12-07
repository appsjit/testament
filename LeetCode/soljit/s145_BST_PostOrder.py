# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import LifoQueue


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root == None:
            return []
        # def postO(pnode):
        #     if pnode == None:
        #         return
        #     postO(pnode.left)
        #     postO(pnode.right)
        #     result.append(pnode.val)
        # postO(root)

        stack = LifoQueue()
        stack.put(root)
        while (not stack.empty()):
            node = stack.get()
            result.append(node.val)
            if node.left != None:
                stack.put(node.left)
            if node.right != None:
                stack.put(node.right)

        return reversed(result)