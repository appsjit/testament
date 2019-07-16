from LinkedListNode import LinkedList
from LinkedListNode import Node
def insertAtTail(list,value):
  # Write - Your - Code
  nnode = Node(value)
  cnode = list.getHead()
  print('-----')
  while cnode.nextElement != None:
    cnode = cnode.nextElement
    print(cnode.data)

  cnode.nextElement = nnode

list = LinkedList()
print("Before : ")
print(list)
insertAtTail(list,9)
print(list)