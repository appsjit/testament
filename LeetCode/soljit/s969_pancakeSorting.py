class Solution:
    def flip(arr, K):
        i = 0
        j = K

        while (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        return arr

    def pancakeSort(self, A: List[int]) -> List[int]:
        bundry = len(A)

        sortProgeress = A[:]
        result = []
        print(sortProgeress)
        print('-----------')
        while (bundry > 0):
            i = 0
            maxNum = float(-inf)
            maxNumIdx = -1
            while (i < bundry):
                if sortProgeress[i] > maxNum:
                    maxNum = sortProgeress[i]
                    maxNumIdx = i
                i += 1
            result.append(maxNumIdx + 1)
            sortProgeress = Solution.flip(sortProgeress, maxNumIdx)
            print(sortProgeress)
            result.append(bundry)
            sortProgeress = Solution.flip(sortProgeress, bundry - 1)
            print(sortProgeress)

            bundry -= 1

        return result