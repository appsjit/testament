class Solution(object):
    global res

    def __init__(self):
        self.res = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mdict = {}
        for x in nums:
            mdict[x] = mdict.get(x, 0) + 1

        print(mdict)
        mlist = []

        self.helper(mlist, mdict)

        return self.res

    def helper(self, plist, pdict):

        if (not pdict):
            print(plist)
            self.res.append(plist[:])

        for nm in pdict.keys():
            plist.append(nm)
            pdict[nm] = pdict.get(nm) - 1
            if (pdict.get(nm) == 0):
                del pdict[nm]

            self.helper(plist, pdict)
            pdict[nm] = pdict.get(nm, 0) + 1
            del plist[len(plist) - 1]





