# Uses python3
import sys

class knapsack():
    def __init__(self,pRatio,pTagId):
        self.ratio = pRatio
        self.tagId = pTagId

def get_optimal_value(capacity, weights, values,n):
    value = 0.
    for x in range(0,n):
        print(x)
        print(weights.__getitem__(x))
        ##print(wt)
    # write your code here

    return value


if __name__ == "__main__":
    ###data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    data = list(map(int, '3 50 60 20 100 50 120 30'.split()))   ### To Hardcode entry
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values,n)
    print("{:.10f}".format(opt_value))
