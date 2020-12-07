# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import LifoQueue


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        #         def helper(pnode):
        #             if pnode == None:
        #                 return

        #             helper(pnode.left)
        #             print(pnode.val)
        #             result.append(pnode.val)
        #             helper(pnode.right)

        #         if root == None:
        #             return []
        #         helper(root)
        #         return result
        curNode = root
        ##stack = deque()
        stack = LifoQueue()
        while (curNode != None or not stack.empty()):
            while (curNode != None):
                print(curNode.val)
                stack.put(curNode)
                curNode = curNode.left

            curNode = stack.get()
            result.append(curNode.val)
            curNode = curNode.right
        return result
