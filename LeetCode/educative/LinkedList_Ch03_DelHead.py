from LinkedListNode import LinkedList

def delete(list,value):
  deleted = False
  if (list.isEmpty()): # Check if list is empty -> Return False
    print ("List is Empty")
    return deleted
  currentNode = list.getHead().nextElement # Get current node
  previousNode = None # Get previous node
  if (currentNode.data == value):
    list.deleteAtHead() # Use the previous function
    deleted = True
    return deleted

  #Traversing/Searching for Node to Delete
  while (currentNode != None):
    #Node to delete is found
    if (value == currentNode.data):
      previousNode.nextElement = currentNode.nextElement # previous node now points to next node
      currentNode.nextElement = None
      deleted = True
      break
    previousNode = currentNode
    currentNode = currentNode.nextElement

  if (deleted == False):
    print (str(value) + " is not in list!")
  else:
    print (str(value) + " deleted!")

  return deleted

list = LinkedList()
list.insertAtHead(1)
list.insertAtHead(4)
list.insertAtHead(3)
list.insertAtHead(2)
list.printList()
delete(list, 4)
##list.printList()