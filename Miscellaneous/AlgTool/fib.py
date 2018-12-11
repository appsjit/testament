# Uses python3
def calc_fib(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a,b = b,a+b

    return output

def getFib(n):
    fibList = []
    fibList.append(1)
    fibList.append(1)

    fNum = 0
    for i in range(2,n):
        fNum = fibList[i-2]+fibList[i-1]
        fibList.append(fNum)

    return fibList[n-1]


n = int(input())

print(calc_fib(n)[n-1])
print(getFib(n))
