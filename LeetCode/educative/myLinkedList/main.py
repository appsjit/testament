import LinkedList as l


def helperFunction(myLinkedList, current, previous):  # This function reverses the linked list recursively
    # Base case
    if current.next is None:
        myLinkedList.head = current
        current.next = previous
        return

    next = current.next
    current.next = previous

    # Recursive case
    helperFunction(myLinkedList, next, current)


def helperFunctionT(myLinkedList, current, previous):  # This function reverses the linked list recursively
    print(myLinkedList)
    print(current.data)
    print(previous)
    print('---------------')

    if (current.next == None):
        myLinkedList.head = current
        current.next = previous
        return


    next = current.next
    current.next = previous

    helperFunctionT(myLinkedList, next, current)


def reverse(myLinkedList):
    # Check if the head node of the linked list is null or not
    if myLinkedList.head is None:
        return

    # Call the helper function --> main recursive function
    helperFunctionT(myLinkedList, myLinkedList.head, None)


# Driver Code
myLinkedList = l.LinkedList()
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(7)
myLinkedList.append(11)

print("Original Linked List")
##myLinkedList.printList()
print("In Process");
reverse(myLinkedList)
print("\nReversed Linked List")
myLinkedList.printList()