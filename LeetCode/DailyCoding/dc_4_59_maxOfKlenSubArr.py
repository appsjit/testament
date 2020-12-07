from collections import deque

def max_of_subarrays(lst, k):
    # O(n k)
    # for i in range(len(lst) - k + 1):
    #     print(max(lst[i: i+k]))

    q = deque()

    ## Preprocessing k length
    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    ##print(q)

    ans = []

    ## q is list of indices where their corresponding values are in descending order
    for i in range(k, len(lst)):
        ##print(lst[q[0]])
        ans.append(lst[q[0]])
        while q and q[0] <=  i - k :
            q.popleft()

        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    ##print(lst[q[0]])
    ans.append(lst[q[0]])
    print(ans)

## Execute within file
testList = [10, 5, 2, 7, 8, 7]
k = 3
max_of_subarrays(testList, k)