
def read_queries():
    n = int(input())
    return n

def findK(v1):
    n = int(input())
    v = [int(input()) for i in range(n)]

    afr = [0]*n
    bfr = [0]*n

    aans = 0

    bans = 0
    for x in range(n):
        if (v[x] == 1 ):
            aans += 1
        else:
            aans -= 1
        afr[x] = aans

        if (v[n - 1 - x] == 1 ):
            bans += 1
        else:
            bans -= 1
        bfr[n - 1 - x] = bans

    print(v)
    print(afr)
    print(bfr)


    if bfr[0] < 1 :
        return 0

    else :
        for y in range(n):
            if (afr[y] > bfr[y]):
                return y
        # for y in range(n):
        #     print(afr[n-1-y])



    return None




##ansList = [1,0,0,1,0]
ansList = [1,1,1,0,1]
##ansList = [1,1,0,1,0]
print(findK(ansList))