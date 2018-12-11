
class HW01:
    def idOf(arr,tgt):
        for indx in range(len(arr)):
            if((arr[indx]) == tgt):
                    return indx

    def getEvenArr(arr):
        evenArr = []
        for indx in range(len(arr)):
            if((arr[indx]) %2 == 0 ):
                evenArr.append(arr[indx])
        return evenArr

    def splitF(str):
        splArr = []
        for x in str:
            splArr.append(x)

        return splArr

    def sumKar(numArr):
        total = 0
        for x in numArr:
            total+=x

        return total

    def merge(l1, l2):
        yield from l1
        yield from l2

    def mergeFun(arr1,arr2):
        ##mergedlist = arr1
        ##mergedlist.extend(arr1)
        ##mergedlist.extend(arr2)
        result = arr1 + arr2
        print(sorted(result))
        return sorted(result)
        ##return list(HW01.merge(arr1,arr2))

if __name__ == '__main__':
    print(HW01.idOf([1, 2, 3, 4, 5, 6], 5))
    print(HW01.getEvenArr([1, 2, 3, 4, 5, 6]))
    print(HW01.splitF('Tanvi'))
    print(HW01.sumKar([1, 2, 3]))
    print(HW01.mergeFun([10, 13, 24], [12, 35]))