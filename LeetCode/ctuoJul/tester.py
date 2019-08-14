
def mergesort(input):
    n = len(input)
    if len(input) > 1 :
        mid = n//2
        leftList = input[:mid]
        rightList = input[mid:]

        mergesort(leftList)
        mergesort(rightList)

        i = 0
        j = 0
        k = 0

        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                input[k] = leftList[i]
                i+=1
            else:
                input[k] = rightList[j]
                j+=1
            k+=1

        while i < len(leftList) :
            input[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList) :
            input[k] = rightList[j]
            j+=1
            k+=1


    return input



if __name__ == '__main__':
    print(mergesort([3,9,1,4,7]))

# def lattice_paths(m, n):  ## row, column
#     # YOUR WORK HERE
#
#     gr = [[0] * n for i in range(m)]
#     ##gr = [[0 for x in range(m)] for y in range(n)]
#
#     print(gr)
#
#     for x in range(m ):
#         gr[x][0] = x
#
#     for y in range(n ):
#         gr[0][y] = y
#
#     print(gr)
#
#     for x in range(m ):
#         for y in range(n ):
#             gr[x][y] += gr[x-1][y] + gr[x][y - 1]
#
#     print(gr)
#
#     return gr[m - 1 ][n - 1]



# def power(base, exponent):
#     # YOUR WORK HERE
#     if (exponent == 1):
#         return base
#     else :
#         return base * power(base, exponent - 1)
#
# if __name__ == '__main__':
#     print(power(3, 3))