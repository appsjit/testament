from myStack import myStack
def isBalanced(exp):
    # Write your code here
    md = {'(': ')', '[': ']', '{': '}'}
    print(exp)
    print('--------')
    stk = myStack()
    for x in exp:
        if x in ('(', '[', '{'):
            stk.push(md.get(x))

        if x in (')', ']', '}'):
            rside = stk.pop()

            if (x != rside):
                return False

    if not stk.isEmpty():
        return False

    return True


#to test your logic
inputString = "{[()]}"
print (inputString + " " + str(isBalanced(inputString)))

inputString = "{[([({))]}}"
print (inputString + " " + str(isBalanced(inputString)))