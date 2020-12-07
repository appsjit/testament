from collections import defaultdict, deque
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self. left = left
        self.right = right


def preOrderTraversal(rNode):

    if rNode == None:
        return

    print(rNode.data)
    if rNode.left != None:
        preOrderTraversal(rNode.left)

    if rNode.right != None:
        preOrderTraversal(rNode.right)

def inOrderTraversal(rNode):

    if rNode == None:
        return

    if rNode.left != None:
        inOrderTraversal(rNode.left)

    print(rNode.data)

    if rNode.right != None:
        inOrderTraversal(rNode.right)

def postOrderTraversal(rNode):

    if rNode == None:
        return

    if rNode.left != None:
        postOrderTraversal(rNode.left)

    if rNode.right != None:
        postOrderTraversal(rNode.right)

    print(rNode.data)

def smallest_level(root):
    q = deque([])
    q.append((root, 0))

    lvl_to_sum = defaultdict(int)

    while q:
        node, lvl = q.popleft()
        lvl_to_sum[lvl] += node.data
        if node.right:
            q.append((node.right, lvl+1))
        if node.left:
            q.append((node.left, lvl+1))



    print(lvl_to_sum)
    return min(lvl_to_sum, key=lvl_to_sum.get)

node2 =  Node(2)
node4 = Node(4)
node5= Node(5)

node3 = Node(3, node4, node5)
node1 = Node(1, node2, node3) ## rootNode



##print(node1)
# preOrderTraversal(node1)
# print('--------')
# inOrderTraversal(node1)
# print('--------')
# postOrderTraversal(node1)

##print(smallest_level(node1))



