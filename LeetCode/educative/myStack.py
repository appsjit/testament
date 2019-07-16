class myStack:
    def __init__(self):
        self.stackList = []

    def isEmpty(self):
        return len(self.stackList) == 0

    def top(self):
        if self.isEmpty():
            return None
        return self.stackList[-1]

    def size(self):
        return len(self.stackList)

    def push(self, value):
        self.stackList.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stackList.pop()