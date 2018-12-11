from operator import mod


class HW03:
    def findOnes(xintArr):
        cntOne = {x : xintArr.count(x) for x in xintArr  }.get(1)
        return 0 if cntOne is None else cntOne

    def getClosestVal(intArr,tgt):
        arr = sorted(intArr)
        closestGap = abs(tgt - arr[0])
        closestNum = int()
        for x in arr:
            ##print(abs(tgt - x))
            if(abs(tgt - x) < closestGap):
                closestGap = abs(tgt - x)
                closestNum = x
                ##print(closestNum)

        return closestNum

    def greaterValues(intArr,tgt):
        return len([x for x in intArr if x > tgt])


    def binSearch(pArr,lIdx,hIdx,pTgt):

        if (lIdx > hIdx):
            return -1

        midIdx = (hIdx + lIdx)//2
        ##print('MidIndx:' + str(midIdx))


        if (pArr[midIdx] == pTgt):
            return midIdx

        if (pArr[lIdx] <= pArr[midIdx] ):  ## Sorted Array
            if ( pArr[lIdx] <= pTgt <= pArr[midIdx] ):
                return HW03.binSearch(pArr,lIdx,midIdx - 1,pTgt)
            return HW03.binSearch(pArr,midIdx + 1,hIdx,pTgt)

        if (pArr[midIdx] <= pTgt <= pArr[hIdx]):
            return HW03.binSearch(pArr, midIdx + 1, hIdx, pTgt)
        return HW03.binSearch(pArr, lIdx , midIdx - 1 , pTgt)
        # Copied from https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

    def getSortedRotatedIndx(intArr,tgt):
        arrLen = len(intArr) - 1
        ##print(arrLen)
        return HW03.binSearch(intArr,0,arrLen,tgt)



if __name__ == '__main__':
    ##print(HW03.getSortedRotatedIndx([1, 2, 3, 4, 5, 6, 7, 8,9], 2))
    print(HW03.getSortedRotatedIndx([35, 46, 79, 102, 1, 14, 29, 31 , 32], 102))
    # print(HW03.greaterValues([1, 2, 3, 5, 5, 7, 9, 10, 11], 5))
    # print(HW03.greaterValues([1, 2, 3], 4 ))
    # print(HW03.greaterValues([1, 10, 22, 59, 67, 72, 100], 13))
    # print(HW03.getClosestVal([1, 2, 3, 5, 5, 7, 9, 10, 11], 6))
    # print(HW03.getClosestVal([1, 2, 3], 8))
    # print(HW03.getClosestVal([1, 10, 22, 59, 67, 72, 100], 70))
    # print(HW03.findOnes([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]))
    # print(HW03.findOnes([0, 0, 0]))
    # print(HW03.findOnes([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]))
