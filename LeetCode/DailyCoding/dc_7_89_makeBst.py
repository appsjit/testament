from dc_6_84_minSumLevel import *
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self. left = left
        self.right = right


def makeBst(array):

    if not array:
        return None

    mid = len(array)//2

    root = Node(array[mid])

    root.left = makeBst(array[:mid])
    root.right = makeBst(array[mid+1:])


    return root

arr = [2,4,7,9]

made = makeBst(arr)

inOrderTraversal(made)