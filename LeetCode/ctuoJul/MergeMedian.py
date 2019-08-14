def mergeMedian(parr1, parr2):
    res = [0] * (len(parr1) + len(parr2))



    i = 0
    j = 0
    r = 0

    while i < len(parr1) and j < len(parr2):
        if parr1[i] < parr2[j]:
            res[r] = parr1[i]
            i += 1
        else:
            res[r] = parr2[j]
            j += 1

        r += 1

    while i < len(parr1):
        res[r] = parr1[i]
        i += 1
        r += 1

    while j < len(parr2):
        res[r] = parr2[j]
        j += 1
        r += 1

    print(res)

    x = len(res)
    while x > 2 :
        res.pop(x-1)
        res.pop(0)
        x -= 2

    return (res[0] + res[1])/2



arr1 = [1, 2, 13, 26, 38]
arr2 = [3, 15, 17, 30, 45]
print(mergeMedian(arr1, arr2))