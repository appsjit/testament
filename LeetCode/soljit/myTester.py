print("Test")

# for i in range(0,10):
#     print(False or True)


## Logic in K Merge Lists
myList = list(range(0, 6))

totSize = len(myList)

interval = 1

while interval < totSize:
    for x in range(0, totSize - interval, interval*2):
        myList[x] =  myList[x] + myList[x + interval]
    interval *=2

print(myList)
print(repr(myList))