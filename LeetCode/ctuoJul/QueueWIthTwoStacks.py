class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.enqueue(val)

    def pop(self) -> int:
        return self.dequeue()

    def enqueue(self, val):
        # self.stack1.append(val)
        self.stack1 += [val]

    def size():
        return len(self.stack1)

    def dequeue(self):
        if self.size == 0:
            return None
        while len(self.stack1) > 0:
            temp = self.stack1[-1]
            self.stack1 = self.stack1[:-1]
            self.stack2 += [temp]

        returnVal = self.stack2[-1]
        self.stack2 = self.stack2[:-1]

        while len(self.stack2) > 0:
            temp = self.stack2[-1]
            self.stack2 = self.stack2[:-1]
            self.stack1 += [temp]

        return returnVal


testQm = MyQueue()
testQm.enqueue(1)
testQm.enqueue(3)
testQm.enqueue(5)
testQm.enqueue(7)

print(testQm.stack1)

# stack 1


# stack 2
# 5, 4, 3, 2