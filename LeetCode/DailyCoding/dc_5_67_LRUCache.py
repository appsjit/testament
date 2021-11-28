from dc_5_67_LinkedList import myLinkedList
from dc_5_67_LinkedList import Node

class LRUCache:
    def __init__(self, n):
        self.n = n
        self.dict = {}
        self.list = myLinkedList()

    def set(self, key, val):
        if key in self.dict:
            self.dict[key].delete

        newNode = Node(key, val)
        self.list.add(newNode)
        self.dict[key] = newNode

        if len(self.dict) > self.n:
            head = self.list.get_head()
            self.list.remove(head)
            del self.dict[head.key]


    def get(self, key):
        if key in self.dict:
            nd = self.dict[key]

            ## Move recently called node to back of Linked List
            self.list.remove(nd)
            self.list.add(nd)

            return nd.val

    def printList(self):
        self.list.printList()


