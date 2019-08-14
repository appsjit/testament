# class MyQueue:
#   def __init__(self):
#     self.stack1 = []
#     self.stack2 = []

#   def push(self, val):
#     self.enqueue(val)

#   def pop(self)->int:
#     return self.dequeue()

#   def enqueue(self, val):
#     # self.stack1.append(val)
#     self.stack1 += [val]

#   def size():
#     return len(self.stack1)


#   def dequeue(self):
#     if self.size == 0:
#       return None
#     while len(self.stack1) > 0 :
#       temp = self.stack1[-1]
#       self.stack1 = self.stack1[:-1]
#       self.stack2 += [temp]

#     returnVal = self.stack2[-1]
#     self.stack2 = self.stack2[:-1]

#     while len(self.stack2) > 0 :
#       temp = self.stack2[-1]
#       self.stack2 = self.stack2[:-1]
#       self.stack1 += [temp]

#     return returnVal


# testQm = MyQueue()
# testQm.enqueue(1)
# testQm.enqueue(3)
# testQm.enqueue(5)
# testQm.enqueue(7)

# print(testQm.stack1)

# stack 1


# stack 2
# 5, 4, 3, 2

'''
Design a min stack class with the following properties:

push(value) - Push an integer onto the stack

pop() - Removes and returns the element on top of the stack

peek() - Return the top value in the stack (do not remove it)

min() - Return the minimum value in the stack

You have access to a Stack class with push(value), pop(), peek(), size() that all run in O(1) time/space.
'''

from heapq import heappush, heappop


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        # heappush(self.stack, val)
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()
        # return heappop(self.stack)

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    # O(n)
    def min(self):
        minVal = float('inf')
        for ele in self.stack:
            if minVal > ele:
                minVal = ele
        return minVal









































