def reverse(list):
  # Write your code here

  prev = None
  cnode = list.getHead().nextElement
  next = None

  while cnode != None:
    next = cnode.nextElement
    cnode.nextElement = prev
    prev = cnode
    cnode = next

    list.getHead().nextElement = prev


  return list