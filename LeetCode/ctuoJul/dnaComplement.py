def dnaComplement(s):
    def getCompl(s):
        if s == 'A':
            return 'T'
        if s == 'T':
            return 'A'
        if s == 'G':
            return 'C'
        if s == 'C':
            return 'G'

    # Write your code here
    myDict = {}
    l1 = []
    for x in s:
        myDict[x] = myDict.get(x, 0) +1

    for k in myDict.keys():
        l1.append(k)
    print(myDict)

    ans = ""

    for m in range(len(l1) -1,-1,-1 ):
        wcnt = myDict[l1[m]]
        while wcnt > 0:

            ans += getCompl(l1[m])
            wcnt -= 1




    # l2 = l1[:]
    # l2.reverse()



    # for m in range(len(l1) -1, -1, -1 ):
    #     wcnt = myDict[l1[m]]
    #     while wcnt > 0:
    #         ans += l2[m]
    #         wcnt -= 1


    return ans






if __name__ == '__main__':
    print(dnaComplement('ACCGGGTTTT'))
    print(dnaComplement('AGTC'))