import string


print(ord('a'))

print("Test")

# for i in range(0,10):
#     print(False or True)


for x in range(3):
    y = x
    y += 1
    print(x)
    print(y)


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

print(string.ascii_lowercase[0::3])

a=  [1, 2, 3]
for index, item in enumerate(a):
    print("Item %s has index %s" % (item, index))


myRange = range(1,11)
print([10*x for x in myRange])


myRange = range(1,11)
print(list(map(str,myRange)))


def addition(n):
    return n + n
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print("map example  "+str(list(result)))


numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print("lambda example  "+str(list(result)))

# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("map with lambda "+str(list(result)))


d = {"a": 1, "b": 2, "c": 3}
print(d.values())
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)

import time
cntr = 0
while True and cntr < 2 :
    print("Hello")
    time.sleep(2)
    cntr += 1


# for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
#     print(letter1 + letter2)

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

global c1
def foo1():
    return c1
c1 = 3
print(foo1())

c2 = 1
def foo2():
    c2 = 33
    return c2
c2 = 3
print(foo2())

