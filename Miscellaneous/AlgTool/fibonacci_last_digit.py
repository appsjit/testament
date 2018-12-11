# Uses python3
import sys

def get_fibonacci_last_digit(n):
    # write your code here
    fibList = []
    fibList.append(0)
    fibList.append(1)

    fNum = 0
    for i in range(2,n+1):
        fNum = fibList[i-2] + fibList[i-1]
        fNum = fNum%10
        fibList.append(fNum)
    return fibList[n]



if __name__ == '__main__':
    ##input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit(n))
