
myDict = {}

def minimumStepsToOne(num):
    # Write your code here

    if num in myDict :
        return myDict.get(num)

    if num == 1:
        myDict[1] = 0
        return 0

    for x in range(2, num +1):
        st = myDict.get(x - 1)

        if (num % 3 == 0):
            st3 = myDict.get(num / 3)
            st = min(st3, st)

        if (num % 2 == 0):
            st2 = myDict.get(num / 2)
            st = min(st2, st)

        myDict[x] = st + 1

    return myDict[num]


print(minimumStepsToOne(30))