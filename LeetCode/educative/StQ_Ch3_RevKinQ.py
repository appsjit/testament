from myStack import myStack
from myQueue import myQueue
def reverseK(queue,k):
  # Write your code here
  mstack = myStack()
  cnt = 0

  while cnt < k:
    mstack.push(queue.dequeue())
    cnt += 1

  while not mstack.isEmpty():
    queue.enqueue(mstack.pop())


  totSize = len(queue.queueList)
  print(totSize)

  for x in range(totSize - k):
    queue.enqueue(queue.dequeue())



#testing our logic
queue = myQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
print ("the queue before reversing:")
print (queue.queueList)
reverseK(queue, 10)
print ("the queue after reversing:")
print (queue.queueList)