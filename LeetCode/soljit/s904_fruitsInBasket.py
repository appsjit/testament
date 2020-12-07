class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        first, second = None, None
        last = {}
        left, res = 0, 0
        for idx, num in enumerate(tree):
            last[num] = idx  ## Updating idex of number ocuurence
            if num not in [first, second]:
                if first != None:
                    left = last[first] + 1  ## Move left side of window to 1 right of last occurence of left
                first = second  # move second to first
                second = num  ## Assign new number to secons
            else:
                if num == first:  ## If current number is first then swap
                    first, second = second, first

            res = max(res, idx - left + 1)

        return res