# Uses python3
import sys

def gcd(a, b):
    print(str(a) + '   ' + str(b))
    if (b == 0):
        return a
    else:
        moda=a%b
        return gcd(b,moda)

if __name__ == "__main__":
    ##input = sys.stdin.read()
    input = str(input())
    a, b = map(int, input.split())
    print(gcd(a, b))
