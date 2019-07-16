class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        t = str.split()
        print(t)

        if (len(pattern) != len(t)):
            return False

        myDict = dict()
        for x in range(len(pattern)):
            sletter = pattern[x]
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
