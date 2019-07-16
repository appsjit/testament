# Access HeadNode => list.getHead()
# Check if list is empty => list.isEmpty()
# Node class  { int data ; Node nextElement;}
def removeDuplicates(list):
    # Write - Your - Code
    print(list)

    satha = []
    cnode = list.getHead().nextElement
    prevnode = list.getHead()

    while cnode != None:
        if cnode.data in satha:
            print("Duplicate")
            prevnode.nextElement = cnode.nextElement  ## Remove Prev Link with Duplicate
        else:
            satha.append(cnode.data)
            prevnode = cnode

        cnode = cnode.nextElement

    return list


########################################################

def removeDuplicates(list):
    currentNode = list.getHead().nextElement
    prevNode = list.getHead()
    # To store values of nodes which we already visited
    visitedNodes = set()
    # If List is not empty and there is more than 1 element in List
    if (not list.isEmpty() and currentNode.nextElement != None):
        while (currentNode != None):
            value = currentNode.data
            if (value in visitedNodes):
                # currentNode is a duplicate as its value is already in the HashSet
                # so connect prevNode with currentNode's next element to remove it
                prevNode.nextElement = currentNode.nextElement
                currentNode = currentNode.nextElement
                continue
            visitedNodes.add(currentNode.data)  # Visiting currentNode for first time
            prevNode = currentNode
            currentNode = currentNode.nextElement

    return list


list = LinkedList()
list.insertAtHead(7)
list.insertAtHead(7)
list.insertAtHead(22)
list.insertAtHead(14)
list.insertAtHead(21)
list.insertAtHead(14)
list.insertAtHead(7)

list.printList()

removeDuplicates(list)
list.printList()
