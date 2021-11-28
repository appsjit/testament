def reconstruct(array):
    res = []
    myStack = []
    n = len(array) - 1

    for i in range(n):
        if array[i+1] == '-':# Next number less than current stack it
            myStack.append(i)
            print('Stacking :'+str(i))
        else: ## Next number higher add to anwer
            res.append(i)
            print('Preparing :' + str(i))
            while myStack:
                res.append(myStack.pop())


    myStack.append(n)

    while myStack:
        res.append(myStack.pop())

    print(res)


##arr = [None, '+', '+', '-', '-']
##arr = [None, '+', '-', '+', '-']
arr = [None, '-', '-', '-', '+']
reconstruct(arr)