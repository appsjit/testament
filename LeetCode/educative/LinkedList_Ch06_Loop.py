#Access HeadNode => list.getHead()
#Check if list is empty => list.isEmpty()
#Node class  { int data ; Node nextElement;}
def detectLoop(list):
  # Write your code here
  cnode = list.getHead()
  visitedNodes = []

  while cnode.nextElement != None:
    print(cnode.data)
    cnode = cnode.nextElement
    if ( cnode in visitedNodes):
      return True
    visitedNodes.append(cnode)

  return False