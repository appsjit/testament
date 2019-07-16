from myStack import myStack
def sortStack(stack):
    if (not stack.isEmpty()):
        # Pop the top element off the stack
        value = stack.pop()

        # Sort the remaining stack recursively
        sortStack(stack)

        # Push the top element back into the sorted stack
        insert(stack, value)


def insert(stack, value):
    if (stack.isEmpty() or value < stack.top()):
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)


stack = myStack()
stack.push(2)
stack.push(97)
stack.push(4)
stack.push(42)
stack.push(12)
stack.push(60)
stack.push(23)

sortStack(stack)

sorted = "sorted stack: [ "
for i in range(stack.size()):
    sorted += str(stack.pop()) + " "

sorted += "]"
print(sorted)