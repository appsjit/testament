# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import LifoQueue


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root == None:
            return []
        #         def preO(pnode):
        #             if pnode == None:
        #                 return

        #             result.append(pnode.val)
        #             preO(pnode.left)
        #             preO(pnode.right)

        #         preO(root)

        stack = LifoQueue()
        stack.put(root)
        while (not stack.empty()):
            node = stack.get()
            if node != None:
                result.append(node.val)
                if (node.right != None):
                    stack.put(node.right)
                if (node.left != None):
                    stack.put(node.left)

        return result