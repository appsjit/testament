def printPascal(testVariable):
    # Write your code here
    if (testVariable == 0):
        return [1]
    elif (testVariable == 1):
        return [1, 1]
    else:
        nlist = [1]
        clist = printPascal(testVariable - 1)

        for x in range(len(clist) - 1):
            nlist.append(clist[x] + clist[x + 1])

        nlist += [1]

        return nlist

    return None