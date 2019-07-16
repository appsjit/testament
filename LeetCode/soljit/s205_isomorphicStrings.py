class Solution:
    def isIsomorphic( s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        myDict = dict()
        for x in range(len(s)):
            sletter = s[x]
            print(sletter)
            if (sletter in myDict.keys()):
                if myDict[sletter] != t[x]:
                    return False
            else:
                print(t[x])
                if t[x] not in myDict.values():
                    myDict[sletter] = t[x]
                else:
                    return False

        return True


if __name__ == '__main__':
    print(Solution.isIsomorphic('ab','aa'))