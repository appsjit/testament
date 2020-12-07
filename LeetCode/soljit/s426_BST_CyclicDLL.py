"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def readTre(pnode):
            nonlocal last, first
            if (pnode == None):
                return None;

            readTre(pnode.left);
            if last:
                last.right = pnode  ##Make next/right node as curNode
                pnode.left = last  ##Link  last -l- pnode
            else:
                ## first occurence assign
                first = pnode
            last = pnode  ## Assign cur node to last

            print(pnode.val)

            readTre(pnode.right)

        if not root:
            return None
        first, last = None, None
        readTre(root)
        ## To make circular
        last.right = first  ## Last  next  First
        first.left = last  ## Last first

        return first
