# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    ##print(str(left)+' '+str(right))
    if (x < a[0] or x > a[right-1] ):
        return -1


def getRighteous():
    pass


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    ##input = sys.stdin.read()
    ##input = str(input())
    ##data = list(map(int, input.split()))
    data = list(map(int, '5 1 5 8 12 13 5 8 1 23 1 11'.split()))
    print(data)
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        ##print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
