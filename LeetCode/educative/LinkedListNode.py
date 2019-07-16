class Node:
    def __init__(self, data):
        self.data = data
        self.nextElement = None


class LinkedList:
    def __init__(self):
        self.headNode = Node(None)

    # Insertion at Head
    def insertAtHead(self, dt):
        tempNode = Node(dt)  # Create a new node containing your specified value
        tempNode.nextElement = self.headNode.nextElement  # The new node points to the same node as the head
        self.headNode.nextElement = tempNode  # Make the head point to the new node
        return self.headNode  # return the new list

    def insertAtTail(list, value):
        # Write - Your - Code
        nnode = Node(value)
        cnode = list.getHead()
        print('-----')
        while cnode.nextElement != None:
            cnode = cnode.nextElement
            print(cnode.data)

        cnode.nextElement = nnode

        return cnode

    def isEmpty(self):
        if (self.headNode.nextElement == None):
            return True
        else:
            return False

    def printList(self):
        if (self.isEmpty()):
            print
            "List is Empty"
            return False
        temp = self.headNode.nextElement
        while (temp.nextElement != None):
            print
            temp.data, "->",
            temp = temp.nextElement
        print
        temp.data, "-> None"
        return True


    def getHead(self):
        return self.headNode


list = LinkedList()
list.printList()

for i in range(1, 10, 1):
    list.insertAtHead(i)
list.printList()