def maxMin(lst):
    # Write your code here
    minIdx = 0
    maxIdx = len(lst) - 1
    nlst = []
    print('-------------')
    for idx in range(len(lst)):
        if idx % 2 == 0:
            print(lst[maxIdx])
            nlst.append(lst[maxIdx])
            maxIdx -= 1
        else:
            print(lst[minIdx])
            nlst.append(lst[minIdx])
            minIdx += 1

    return nlst

    maxMin([1, 2, 3, 4, 5, 6, 7])
    maxMin([1, 2, 3, 4, 5])
