import re
class HW02:
    def getUnique(str):
        return list(set(str))

    def wrdCnt(selfstr):
        selfstr = selfstr.lower()
        ##selfstr = re.sub('\W+',' ',selfstr)  ## to replace special characters with space
        selfstr = re.sub(r'[?|$|.|!]', r'', selfstr)  ## above also works
        str2 = selfstr.split()   ## Split creates list
        unique_wrd = set(str2)   ## to get Unique
        ##print(unique_wrd)

        mdict = dict()
        for x in unique_wrd:
            mdict[x] = str2.count(x)

        return mdict


    def chkRgb(str):
        str1 = list(str)
        return min(str1.count('r'),str1.count('g'),str1.count('b'))
        # for x in str1:
        #     print(x)
        ##print(re.search('rgb',str))
        # return str.count('rgb')


    def getMisisngNumber(n,arr):
        arr1 = sorted(arr)
        minNum = arr1[0]
        ##print(minNum)
        arrExp = list()
        for x in range(minNum,minNum+n):
            arrExp.append(x)

        setCurr = set(arr1)
        setReqd = set(arrExp)
        ##print(setCurr)
        setReqd.difference_update(setCurr)
        return list(setReqd)
        ##print(setReqd)


    def letterSort(str):
        return ''.join(sorted(list(str)))

    def getCharMode(str):
        strMod = str.lower().replace(' ','')
        cList = list(strMod)
        unqWrd = set(cList)
        # print(cList)
        # print(unqWrd)

        strMax = ''
        strMaxOccur = 0
        for x in unqWrd:
            if strMod.count(x) > strMaxOccur:
                strMax = x
                strMaxOccur = strMod.count(x)
            elif (strMod.count(x) == strMaxOccur):
                strMax += x

        # print(strMax)
        # print(strMaxOccur)
        return strMax


    def sortDigits(intx):
        return ''.join(sorted(list(str(intx).replace('0',''))))


    def getDupl(arr):
        freqDict = {x:arr.count(x) for x in arr}
        return [x for x in freqDict.keys() if freqDict[x] >1]

    def checkAnagrams(str1,str2):
        return True if sorted(str1) == sorted(str2) else False

    def checkPalindrome(str):
        return True if (str == ''.join(reversed(str))) else False

if __name__ == '__main__':
    ##print(HW02.getUnique([1, 2, 3, 1, 2]))
    # print(HW02.wrdCnt('The cat and the hat.'))
    # print(HW02.wrdCnt('As soon as possible.'))
    # print(HW02.wrdCnt('It''s a man, it''s a plane, it''s superman!'))
    # print(HW02.chkRgb('rbgrbrgrgbgrrggbbbbrgrgrgrg'))
    # print(HW02.getMisisngNumber(4, [1, 4, 2]))
    # print(HW02.getMisisngNumber(8, [4, 7, 1, 6]))
    # print(HW02.getMisisngNumber(6, [6, 4, 2, 1]))
    ##print(HW02.letterSort('hello'))
    # print(HW02.getCharMode('A walk in the park'))
    # print(HW02.getCharMode('hello'))
    # print(HW02.getCharMode('noon'))
    # print(HW02.sortDigits(7890))
    # print(HW02.sortDigits(32445))
    # print(HW02.sortDigits(10101))
    # print(HW02.getDupl([1, 2, 4, 2]))
    # print(HW02.getDupl([3, 2, 3, 2, 3, 3, 4]))
    # print(HW02.getDupl([1, 2, 3, 4]))
    # print(HW02.checkAnagrams('cat','act'))
    # print(HW02.checkAnagrams('cat', 'cam'))
    # print(HW02.checkAnagrams('racecar', 'aaccrres'))
    # print(HW02.checkAnagrams('listen', 'silent'))
    print(HW02.checkPalindrome('racecar'))
    print(HW02.checkPalindrome('cat'))
    print(HW02.checkPalindrome('malayalam'))
