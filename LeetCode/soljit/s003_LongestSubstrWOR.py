class Solution:
    def lengthOfLongestSubstring( s):

        patDict = {}

        strArray = list(s)
        ans = 0
        latestOccurenceIdx = 0
        for idx in range(len(strArray)):
            currLetter = strArray[idx]
            print('---------------idx:' + str(idx))
            print('Befor ans:' + str(ans), '    latestOccurenceIdx:' + str(latestOccurenceIdx) + '  of char ' + currLetter)
            if (currLetter in patDict.keys()):   ## if letter exists in word calculate latest occurence of any letter  before update to move slider
                latestOccurenceIdx = max(patDict[currLetter], latestOccurenceIdx)


            ## latest occurence concludes first longest occurenc and starts looking for second longest if exists
            ans = max(ans, idx - latestOccurenceIdx + 1)

            patDict[currLetter] = idx + 1   ##  add letters latest occurence in dictionary
            print('After ans:' + str(ans), '    latestOccurenceIdx:' + str(latestOccurenceIdx) + '  of char ' + currLetter)

        return ans



if __name__ == '__main__':
    Solution.lengthOfLongestSubstring('abcbbcabcsab')


