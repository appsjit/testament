import math
import heapq
import collections
def stringGround(pStr):
    print('Input String is :'+pStr)
    if 'c' in pStr: ## Case Censitive
        print('c exists')
    lenStr = len(pStr)
    print('Index of e at '+str(pStr.index('e')))

    print('Substring till occurence of B  :'+pStr[:pStr.index('B')])

    print('Trim Last Letter  : '+pStr[:-1])

    print('Print Last Letter  : ' + pStr[-1])
    print('Print Third index/4th Letter  : ' + pStr[3])
    print('Print Third Last Letter  : ' + pStr[-3])

    print('Print Using Substr  : ' + pStr[0:lenStr+1])
    s = 'abc'
    print('Print Using Substr 2   : ' + s[0:2])

    print('Lpad for 2 '+'9'.rjust(3,'0'))

    print('Ceil     1.2:' + str(math.ceil(1.2)))
    print('Rounding 1.2:'+str(round(1.2)))
    print('Rounding 1.5:' + str(round(1.5)))

    ## Del one char and print
    for i in range(len(pStr)):
        ## Delete one char and check if it exist in map
        tWord = pStr[:i] + pStr[i + 1:]
        print(tWord)

def sortMan():
    courses = [[5,8],[4,6],[2,6]]
    print(courses)
    ## Sort based on 1th index
    courseSorted = sorted(courses, key = lambda x : x[1])
    print(courseSorted)


    ## Sorting words based on word length
    words = ["bdcae","a","b","ba","bca","bda","bdca"]
    words = sorted(words, key=lambda x: len(x))
    print(words)

## https://docs.python.org/2/library/heapq.html
## https://www.educative.io/edpresso/what-is-the-python-priority-queue
from queue import PriorityQueue
def priorityQueue():
    q = PriorityQueue()

    q.put((1.34, ' A'))
    q.put((3.34, ' C'))
    q.put((2.26, ' B'))

    while not q.empty():
        print(q.get())

def bfsQueue():
    q = collections.deque([('CAR', 1)])
    q.append(('Mustang', 2))

    while q:
        current_word, level = q.popleft()
        print(current_word, level)

def simpleQueList():
    queue = []
    queue.append('a')
    queue.append('b')
    queue.append('c')

    while len(queue) > 0:
        print(queue.pop(0))


def heapGround():
    ##nums = [3,2,1,5,6,4]
    nums = [3,4,1,2]
    h = []

    for i in nums:
        heapq.heappush(h, i)

    print(h)


def dictGround():
    myDict = {}

    myDict['x'] = myDict.get('x', 0) + 11   ## Increment value even if key exists or not
    myDict['y'] = 22

    if 'y' in myDict:
        print('y exists with value :'+str(myDict['y']))

    for k,v in myDict.items():
        print(v)


    ##prefix has Array
    prefixHashTable = {}
    def buildPrefixHashTable(words):
        ##self.prefixHashTable = {}
        for word in words:
            # for prefix in (word[:i] for i in range(1, len(word))):
            #     prefixHashTable.setdefault(prefix, set()).add(word)
            for i in range(1, len(word)):
                prefix = word[:i]
                print(prefix)
                prefixHashTable.setdefault(prefix, set()).add(word)


    wor = ["ball","area","lead","lady"]
    buildPrefixHashTable(wor)
    print(prefixHashTable)

    prefix = ''.join([word[1] for word in wor])
    print(prefix)
    print(set([]))


    ## To get Dict Values as list
    print(list(myDict.values()))

    ce = [""]
    for c in ce :
        print("")

    counts = {}  # Creating a dictionary
    # Initializing dictionary with pairs like (lst[i],count)
    counts = counts.fromkeys(wor, 0)

    print(counts)

    ## Creating ordered dictionary
    orderedCounts = collections.OrderedDict()  # Creating an ordered dictionary
    # Initializing dictionary with pairs like (lst[i],0)
    orderedCounts = orderedCounts.fromkeys(wor, 0)
    print(orderedCounts)

    myDefaultDict = collections.defaultdict(list)

    word = 'CAR'
    for i in range(len(word)):
        myDefaultDict[word[:i]+"*"+word[i+1:]].append(word)

    print(myDefaultDict)

def kDistSortLambda():
    points = [[3,3],[5,-1],[-2,4]]
    k       =   2
    points.sort(key = lambda x : math.pow(x[0],2) + math.pow(x[1],2))

    print(points)


def whileLoopPlayer():
    l = 8

    interval = 1
    while interval < l:
        for x in range(0, l - interval , interval*2  ):
            print(str(x)+"  "+str(x+interval) )
        interval = interval*2


def simpleStack():
    stack = []

    stack.append(11)
    stack.append(12)
    stack.append(13)

    if stack :
        print(stack[-1])    ## Peek

    stack.pop()



def gridArray(inpGrid, pNum):
    # print(inpGrid[0])
    # print(inpGrid[1])
    # print(inpGrid[2])
    # print(inpGrid[3])
    r = len(inpGrid)
    c = len(inpGrid[0])
    print('Building empty Grid')
    ##grid = [[1]*c]*r

    grid = [[False for x in range(c)] for y in range(r)]
    ##grid = inpGrid[:]      #############   To Copy Object
    print(grid)
    for i in range(0, r):
        for j in range(0, c):
            print(str(inpGrid[i][j])+'  '+str(grid[i][j]))
    print(inpGrid)
    pNum += 10


def loopMaster():
    nums = [101, 92, 83, 74, 65]

    for x in nums:
        print(x)

    for index, valu in enumerate(nums):
        print(str(index) + '  ' + str(valu))

    g = 2
    for i in range(g, g+1):
        print(i)


pS = 500
##gridArray([[1,2,3,4],[5,6,7,8],[9,10,11,12]], pS)
##print(pS)
##simpleStack()
##dictGround()
stringGround('AceOfBase')
##priorityQueue()
##bfsQueue()
##kDistSortLambda()
##whileLoopPlayer()
##heapGround()
##simpleQueList()
##sortMan()
##loopMaster()




## Notes  , Good Quick Trie at 212 word search
print('-----------')
# from soljit import s084_HistogramLargestRectangle
# sol = s084_HistogramLargestRectangle.Solution()
# print('From different folders '+str(sol.largestRectangleArea([2,1,5,6,2,12])))
