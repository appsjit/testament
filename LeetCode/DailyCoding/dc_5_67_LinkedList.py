class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class myLinkedList :
    def __init__(self):
        ## create dummy nodes and set up head and tail
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')

        self.head.next = self.tail
        self.tail.prev = self.head

    def get_head(self):
        return self.head.next

    def get_tail(self):
        return self.tail.prev

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(Self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def printList(self):
        hnode = self.head
        while hnode.next :
            print(hnode.next.val)
            hnode = hnode.next