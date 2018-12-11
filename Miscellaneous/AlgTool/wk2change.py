# Uses python3
import math
import sys

def get_change(n):
    #write your code here
    a10 = math.trunc(n/10)  ## ****** Java Math.round worked
    ap10 = n%10

    a5 = math.trunc(ap10/5)
    ap5 = ap10%5

    return a10 + a5 + ap5

if __name__ == '__main__':
    #n = int(sys.stdin.read())
    n = int(input())
    print(get_change(n))
